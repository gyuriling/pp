class ContactInfo:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def print_info(self):
        print('{0} : {1}'.format(self.name, self.email))

if __name__ == '__main__':
    gyuri = ContactInfo('김규리', 'gyuriling@naver.com')
    hanbit = ContactInfo('hanbit', 'noreply@hanb.co.kr')

    gyuri.print_info()
    hanbit.print_info()
