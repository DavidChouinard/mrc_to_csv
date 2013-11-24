from pymarc import MARCReader
import csv, os

def main():

    for filename in os.listdir('data/mrc/'):
        if os.isdir('data/mrc/' + filename):
            break

        reader = MARCReader(file('data/mrc/' + filename))

        with open('data/csv/' + os.path.splitext(filename)[0] + '.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(['isbn', 'title', 'author',
                            'publisher', 'pubplace', 'pubyear',
                            'extent', 'dimensions', 'subject', 'inclusiondate',
                            'source', 'library', 'notes'])

            for i, record in enumerate(reader):
                #print record
                pubplace = clean(record['260']['a']) if '260' in record else None
                extent = clean(record['300']['a'], True) if '300' in record else None
                dimensions = record['300']['c'] if '300' in record else None
                subject = record['650']['a'] if '650' in record else None
                inclusiondate = record['988']['a'] if '988' in record else None
                source = record['906']['a'] if '906' in record else None
                library = record['690']['5'] if '690' in record else None

                notes = " ".join([field['a'] for field in record.notes() if 'a' in field])

                writer.writerow([record.isbn(), get_title(record), clean(record.author(), True),
                                clean(record.publisher()), pubplace, clean(record.pubyear()),
                                extent, dimensions, subject, inclusiondate,
                                source, library, notes])

                if i % 100 == 0:
                    print filename + ": " + str(i) + " documents processed"

def get_title(record):
    # pymarc has a title() method that is similar to this, but it doesn't
    # concatenate subtitle and title properly
    if '245' in record and 'a' in record['245']:
        title = clean(record['245']['a'])
        if 'b' in record['245']:
            title += ' ' + clean(record['245']['b'])
        return title
    else:
        return None

def clean(element, isAuthor=False):
    if element is None:
        return element
    else:
        element = element.strip()

        for character in [',', ';', ':', '/']:
            if element[-1] == character:
                return element[:-1].strip()

        if not isAuthor and element[-1] == '.':
            # don't strip trailing periods from author names
            return element[:-1].strip()

        return element.strip()

if __name__ == "__main__":
    main()
