from .models import Course, Video


def save_courses(doc, excel=False):
    if not excel:
        with open(doc, 'r') as f:
                for line in f:
                    s=line.split(',')
                    if s[0]:
                        print(s[0], s[1])
                        Course.objects.create(title=s[0], url=s[1])


def save_videos(doc, excel=False):
    if not excel:
        with open(doc, 'r') as f:
                for line in f:
                    s=line.split(',')
                    if s[0]:
                        title=s[0]
                    print(title, s[4], s[5])
                    course=Course.objects.get(title=title)
                    Video.objects.create(course=course, title=s[4], url=s[5])
