from __future__ import print_function
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import read_write_data as rwlib
import sys

__author__ = 'Grzegorz'

def analyse_sentiment(crawled_data):

    # comments = [row[1] for row in crawled_data[:30]]

    sid = SentimentIntensityAnalyzer()

    trump_summary = dict()
    clinton_summary = dict()


    for date, comment in crawled_data[:]:
        print("######  ", date)
        # print(comment.encode(sys.stdout.encoding, errors='replace'))
        comment_sentences = filter(lambda s: len(s) > 0, comment.split('.'))      # get non empty sentences
        about_trump_previously = about_clinton_previously = False

        whole_comment_trump_sentiment = whole_comment_trump_sentences_counter = 0
        whole_comment_clinton_sentiment = whole_comment_clinton_sentences_counter = 0

        for sentence in map(lambda x: x.lower(), comment_sentences):        # convert sentences to lower case
            about_trump = about_clinton = False
            if any(keyword in sentence for keyword in ["trump", "republicans"]):
                about_trump = True
            if any(keyword in sentence for keyword in ["clinton", "democrats"]):
                about_clinton = True

            if about_clinton or about_trump or about_trump_previously or about_clinton_previously:        # in other case there is no sense of sentiment analisys
                # print("## ", sentence.encode(sys.stdout.encoding, errors='replace'))        #some characters are encoded in strange standard
                # print('Trump:++, ' if about_trump else 'Trump:--, ', end='')
                # print('Clinton:++, ' if about_clinton else 'Clinton:--, ', end='')

                if about_trump and about_clinton:               # for both matches - ignore sentence - too difficult
                    about_trump_previously = about_clinton_previously = False
                    continue
                if not about_trump and not about_clinton:       # if no match in this sentence - use previous match (we know it exists and its only one of them)
                    about_trump = about_trump_previously
                    about_clinton = about_clinton_previously
                else:                                           # match in this sentence
                    about_trump_previously = about_trump
                    about_clinton_previously = about_clinton

                ss = sid.polarity_scores(sentence)
                # for key in sorted(ss):
                #     print('{0}: {1}, '.format(key, ss[key]), end='')
                # print()
                if about_trump:
                    if ss['compound'] == 0:
                        continue
                    if ss['compound'] > 0:
                        print("Trump ++++")
                        # trump_summary[date] = trump_summary[date] + 1 if date in trump_summary else 1
                    else:
                        print("Trump ----")
                        # trump_summary[date] = trump_summary[date] - 1 if date in trump_summary else -1
                    # trump_summary[date] = trump_summary[date] + ss['compound'] if date in trump_summary else ss['compound']
                    whole_comment_trump_sentiment += ss['compound']
                    whole_comment_trump_sentences_counter += 1
                else:
                    if ss['compound'] == 0:
                        continue
                    if ss['compound'] > 0:
                        print("Clinton ++++")
                        # clinton_summary[date] = clinton_summary[date] + 1 if date in clinton_summary else 1
                    else:
                        print("Clinton ----")
                        # clinton_summary[date] = clinton_summary[date] - 1 if date in clinton_summary else -1
                    # clinton_summary[date] = clinton_summary[date] + ss['compound'] if date in clinton_summary else ss['compound']
                    whole_comment_clinton_sentiment += ss['compound']
                    whole_comment_clinton_sentences_counter += 1

        whole_comment_trump_sentiment /= (whole_comment_trump_sentences_counter or 1)
        trump_summary[date] = trump_summary[date] + whole_comment_trump_sentiment if date in trump_summary else whole_comment_trump_sentiment
        whole_comment_clinton_sentiment /= (whole_comment_clinton_sentences_counter or 1)
        clinton_summary[date] = clinton_summary[date] + whole_comment_clinton_sentiment if date in clinton_summary else whole_comment_clinton_sentiment

    print("\n################# Trump summary:")
    for key in sorted(trump_summary.keys()):
        print(key, " - ", trump_summary[key])

    print("\n################# Clinton summary:")
    for key in sorted(clinton_summary.keys()):
        print(key, " - ", clinton_summary[key])

    return (trump_summary, clinton_summary)



