import sys

result_list = []
with open(sys.argv[1]) as f:
    result_list = f.read().split('\n')

emails = [
    '',
    'info@neoland.ru',
    'service@linguachicago.com',
    'info@libete.ru',
    'info@proflingva.ru'
]

for email in emails:
    try:
        result_list.remove(email)
    except ValueError:
        pass

result_list = map(lambda email: email.rstrip(), result_list)

with open('clean_emails.txt', 'w') as f:
    for result in result_list:
        f.write(result + ' ')
