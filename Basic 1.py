from bs4 import BeautifulSoup

with open('Home1.html', 'r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    # for course in courses_html_tags:
    #     print(course.text)

    course_cards = soup.find_all('div', class_='card')

    money = int(input("Enter the money you have : "))
    check = False
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split(' ')[-1]

        if int(course_price[:-1]) <= money:
            print(f'you can buy {course_name} course for {course_price}')
            check = True

    if not check:
        print("You don't have enough money to buy any course!!!")

    