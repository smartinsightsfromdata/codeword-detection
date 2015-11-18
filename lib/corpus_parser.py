__author__ = 'linanqiu'


def parse_wsj():
    from nltk.corpus import ptb
    import logging

    logger = logging.getLogger('root')

    all_lines = []

    for wsj_folder in range(0, 25):
        for file_number in range(0, 100):
            wsj_file = 'wsj/%02d/wsj_%02d%02d.mrg' % (wsj_folder, wsj_folder, file_number)
            logger.info('opening %s' % wsj_file)
            try:
                line = [word.lower() for word in ptb.words(wsj_file)]
                all_lines.append(line)
            except IOError:
                logger.info('not found')

    return all_lines
