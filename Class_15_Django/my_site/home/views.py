from django.shortcuts import render


def home_view(request):
    """
    Відображає головну сторінку сайту.

    Args:
        request: Об'єкт HTTP-запиту.

    Returns:
        Відрендорений шаблон home.html.
    """
    return render(request, 'home/home.html')


def about_view(request):
    """
    Відображає сторінку "Про нас".

    Args:
        request: Об'єкт HTTP-запиту.
    """
    return render(request, 'home/about.html')


def contact_view(request):
    """
    Відображає сторінку "Контакти".

    Args:
        request: Об'єкт HTTP-запиту.
    """
    return render(request, 'home/contact.html')


def post_view(request, id: int):
    """
    Відображає сторінку поста за його ідентифікатором.

    Args:
        request: Об'єкт HTTP-запиту.
        id (int): Ідентифікатор поста.
    """
    return render(request, 'home/post.html', {'id': id})


def profile_view(request, username: str):
    """
    Відображає сторінку профілю користувача за його іменем.

    Args:
        request: Об'єкт HTTP-запиту.
        username (str): Ім'я користувача.
    """
    return render(request, 'home/profile.html', {'username': username})


def event_view(request, year: int, month: int, day: int):
    """
    Відображає сторінку події за вказаною датою.

    Args:
        request: Об'єкт HTTP-запиту.
        year (int): Рік події.
        month (int): Місяць події.
        day (int): День події.

    Returns:
        Відрендерений шаблон event.html з контекстом {'year': year, 'month': month, 'day': day}.
    """
    return render(request, 'home/event.html', {
        'year': year,
        'month': month,
        'day': day
    })
