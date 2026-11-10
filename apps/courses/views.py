from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def course_list(request):
    courses = [
        {
            'id': 1,
            'level': 'Principiante',
            'rating': 4.4,
            'course_title': 'Python fundamentos hasta los detalles',
            'instructor': 'Ernesto Alfonso',
            'course_image': 'images/curso_1.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 2,
            'level': 'Intermedio',
            'rating': 4.7,
            'course_title': 'Desarrollo Web con Django y SQLite',
            'instructor': 'Mariana Silva',
            'course_image': 'images/curso_2.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 3,
            'level': 'Avanzado',
            'rating': 4.9,
            'course_title': 'Ciencia de Datos y Machine Learning con Pandas',
            'instructor': 'Carlos Mendoza',
            'course_image': 'images/curso_3.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 4,
            'level': 'Principiante',
            'rating': 4.5,
            'course_title': 'Automatización de Tareas y Scripts en Python',
            'instructor': 'Beatriz Gómez',
            'course_image': 'images/curso_4.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 5,
            'level': 'Intermedio',
            'rating': 4.6,
            'course_title': 'Creación de APIs RESTful con FastAPI',
            'instructor': 'Alejandro Ríos',
            'course_image': 'images/curso_5.jpg',
            'instructor_image': 'https://randomuser.me/api/portraits/women/68.jpg'
        }
    ]

    return render(request, 'courses/courses.html', {
        'courses': courses
    })


def course_detail(request):
    course = {
        'course_title': 'Django Aplicaciones',
        'course_link': 'course_lessons',
        'course_image': 'images/curso_2.jpg',
        'info_course': {
            'lessons': 79,
            'duration': 8,
            'instructor': 'Ernesto Alfonso'

        },
        'course_content': [
            {
                'id': 1,
                'name': 'Introduccion al curso',
                'lessons': [
                    {
                        'name': '¿Qué aprenderas en el curso?',
                        'type': 'video'
                    },
                    {
                        'name': '¿Cómo usar la plataforma?',
                        'type': 'article'
                    }
                ]

            }
        ]
    }
    return render(request, 'courses/course_detail.html', {
        'course': course
    })


def course_lessons(request):
    lesson = {
        'course_title': 'Django Aplicaciones',
        'course_progess': 30,
        'course_link': 'course_lessons',
        'course_image': 'images/curso_2.jpg',
        'course_content': [
            {
                'id': 1,
                'name': 'Introduccion al curso',
                'total_lessons': 8,
                'complete_lessons': 3,
                'lessons': [
                        {
                            'name': '¿Qué aprenderas en el curso?',
                            'type': 'video'
                        },
                    {
                            'name': '¿Cómo usar la plataforma?',
                            'type': 'article'
                        }
                ]

            }
        ]
    }
    return render(request, 'courses/course_lesson.html', {
        'lesson': lesson
    })
