
def clean_file():
    fi = open('not_in_db.txt', 'r')
    unique = set()
    for w in fi.readlines():
        unique.add(w.strip('\n'))
    fi.close()

    fi_clean = open('not_in_db_clean.txt', 'w')
    for u in sorted(unique):
        if ' ' not in u:
            fi_clean.write(u + "\n")
    fi_clean.close()


if __name__ == '__main__':
    print "Hello"

