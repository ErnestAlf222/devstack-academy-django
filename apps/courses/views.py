from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Course
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def course_list(request):
    # Traemos todos los cursos de la base de datos
    courses = Course.objects.all()
    query = request.GET.get('q')
    if query:
        # Filtramos los cursos por título o por nombre del instructor (primer nombre o apellido) que contengan la cadena de búsqueda
        courses = courses.filter(
            Q(title__icontains=query) | Q(owner__first_name__icontains=query) | Q(
                owner__last_name__icontains=query)
        )
    paginator = Paginator(courses, 10)  # Mostramos 10 cursos por página
    page_number = request.GET.get('page')
    # Obtenemos la página de cursos correspondiente al número de página solicitado
    course_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    # Eliminamos el parámetro 'page' de la cadena de consulta para que no se duplique en los enlaces de paginación
    if 'page' in query_params:
        query_params.pop('page')
    query_string = query_params.urlencode()

    # Renderizamos la plantilla 'courses/courses.html' con los cursos y la cadena de búsqueda como contexto
    return render(request, 'courses/courses.html', {
        'course_obj': course_obj,
        'query': query,
        'query_string': query_string
    })


def course_detail(request, slug):
    # Obtenemos el curso correspondiente al slug proporcionado o devolvemos un error 404 si no existe
    course = get_object_or_404(Course, slug=slug)
    modules = course.modules.prefetch_related('contents')
    # Expresion generadora para contar el número total de contenidos en todos los módulos del curso
    total_contents = sum(module.contents.count() for module in modules)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'modules': modules,
        'total_contents': total_contents
    })


def course_lessons(request, slug):
    course = get_object_or_404(Course, slug=slug)
    course_title = course.title
    # Obtenemos el primer módulo del curso y su primer contenido (lección)
    modules = course.modules.prefetch_related('contents')

    return render(request, 'courses/course_lesson.html', {
        'course_title': course_title,
        'modules': modules
    })
