from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from collections import Counter
from django.views import View
from most_common_words.models import TopWords
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


class FlashcardsListView(LoginRequiredMixin, View):

    def most_used_words(self, request):
        if request.method == 'GET':
            if request.GET.get("name_doc"):
                self.name_doc = request.GET.get("name_doc")
                with open("/home/mati/PycharmProjects/Flashcards/" + self.name_doc) as f:
                    file_to_str = f.read()
                    list_clear_words = split(r'[,."=[(:?!/;\s]\s*', file_to_str)
                list_lower_case = [n.lower() for n in list_clear_words if len(n) > 2]
                self.count_all_words = len(list_lower_case)
                list_unique_words = list(set(list_lower_case))
                self.count_unique_words = len(list_unique_words)
                list_without_known_words = [x for x in list_lower_case if x not in know_words]
                word_counts = Counter(list_without_known_words)  # do zapisania do bazy/ słówka bez liczb
                list_most_common_words = word_counts.most_common(300)
                return list_most_common_words

    def get(self, request):
        if request.method == 'GET':
            if request.GET.get("id_project"):
                self.id_project = request.GET.get("id_project")
                list_most_common_words = self.most_used_words(request)
                current_user = request.user
                id_project1 = self.id_project
                all_words = self.count_all_words
                unique_words = self.count_unique_words
                for x,y in list_most_common_words:
                    a = TopWords(word_eng=x, word_frequency=y, user_id=current_user.id, name_project_id=id_project1)
                    a.save()
                ctx = {
                    "top_flashcards": list_most_common_words,
                    "all_words": all_words,
                    "unique_words": unique_words,
                }
                return render(request, "thanks.html", ctx)


@login_required
def segregate(request):
    name_project_1 = request.GET.get("name_project_1")
    topWords_1 = TopWords.objects.filter(name_project_id = name_project_1)
    return render(request, 'segregate.html', { 'topWords_1': topWords_1 })

