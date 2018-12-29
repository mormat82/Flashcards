from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from collections import Counter
from django.views import View
from most_common_words.models import TopWords, Statistics
from django.contrib.auth.decorators import login_required
from re import split

know_words = ['public', 'that', 'you', 'the', 'and', 'which', 'with', 'their', 'will', 'this',
              'have', 'they', 'from', 'business', 'would', 'what', 'because',
              'should', 'more', 'american', 'were', 'only', 'been', 'these',
              'group', 'make', 'this', 'some', 'opinion', 'large',
              'than', 'work', 'ideas', 'most', 'them', 'there', 'when', 'very',
              'those', 'idea', 'there', 'every', 'public', 'does', 'women',
              'good', 'many', 'business', 'radio', 'life', 'number',
              'known', 'fashion', 'under', 'best', 'understand', 'cannot',
              'millions', 'makes', 'then', 'take', 'education', 'college',
              'like', 'years', 'school', 'true', 'great', 'time', 'world',
              'they', 'propaganda', 'must', 'made', 'other', 'news', 'ebook', 'big']


# class FlashcardsListView(LoginRequiredMixin, View):
@login_required
def get_name_doc(request):
    if request.method == 'GET':
        if request.GET.get("name_doc"):
            name_doc = request.GET.get("name_doc")
            return name_doc

def get_id_project(request):
    if request.method == 'GET':
        if request.GET.get("id_project"):
            id_project = request.GET.get("id_project")
            return id_project

def get_list_words(request):
    with open("/home/mati/PycharmProjects/Flashcards/" + get_name_doc(request)) as f:
        file_to_str = f.read()
        list_words = split(r'[,."=[(:?!/;\s]\s*', file_to_str)
        list_lower_case = [n.lower() for n in list_words if len(n) > 2]
        return list_lower_case

def save_most_common_words(request):
    list_total_words = get_list_words(request)
    list_unique_words = list(set(list_total_words))
    list_without_known_words = [x for x in list_unique_words if x not in know_words]
    word_counts = Counter(list_total_words)  # do zapisania do bazy/ słówka bez liczb
    list_most_common_words = word_counts.most_common(1000)
    current_user = request.user
    id_project1 = get_id_project(request)
    for x,y in list_most_common_words:
        a = TopWords(word_eng=x, word_frequency=y, user_id=current_user.id, name_project_id=id_project1)
        a.save()
    total_amount_of_words = len(list_total_words)
    amount_of_unique_words = len(list_unique_words)
    amount_of_unknown_words = len(list_without_known_words)  # do zapisania do bazy/ słówka bez liczb
    b = Statistics(total_amount_of_words=total_amount_of_words, amount_of_unique_words=amount_of_unique_words, amount_of_unknown_words=amount_of_unknown_words, name_project_id=id_project1)
    b.save()
    return render(request, "thanks.html")

@login_required
def segregate(request):
    name_project_1 = request.GET.get("name_project_1")
    top_words = TopWords.objects.filter(name_project_id = name_project_1)
    statistics = Statistics.objects.filter(name_project_id = name_project_1)
    ctx = {
        "statistics": statistics,
        "top_words": top_words,
    }
    return render(request, 'segregate.html', ctx)

