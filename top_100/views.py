from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from collections import Counter
from django.views import View



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
                name_doc = request.GET.get("name_doc")
                with open("/home/mati/PycharmProjects/FISZKI/" + name_doc) as f:
                    list_clear_words = [word.replace(",", "").
                                 replace(".", "").
                                 replace('"', '').
                                 replace("=", "").
                                 replace("/", "")
                             for line in f for word in line.split()]
                list_lower_case = [n.lower() for n in list_clear_words if len(n) > 3]

                list_unique_words = list(set(list_lower_case)) #usuwamy duplikujące się wyrazy
                print("lista bez duplikatów to", len(list_unique_words), "słów")
                list_without_known_words = [x for x in list_lower_case if x not in know_words]
                print(len(list_without_known_words))
                word_counts = Counter(list_without_known_words)  # do zapisania do bazy/ słówka bez liczb
                top_100 = word_counts.most_common(150)  # już na tym można działać, wyświetlić listę na stronie
                print(top_100)
                return top_100


    def get(self, request):
        top_100 = self.most_used_words(request)
        ctx = {
            "top_flashcards": top_100,
        }
        return render(request, "top_words.html", ctx)


# def save_to_base():
#     for x,y in top_100:
#         a = TopWords(word_eng=x, word_frequency=y)
#         a.save()

# save_to_base()
