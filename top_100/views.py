
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from collections import Counter
from django.views import View
# from upload_file.models import Document
# from upload_file.models import Document as docs
# from django.views.generic.edit import CreateView # DeleteView
# from top_100.models import TopWords


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

# file_documents = Document.object.name

class FlashcardsListView(View):

    def create_flashcards(self):
        # book_title = Document.objects.get(pk=book_id)
        # print(book_title)
        file_documents = "Joseph_Conrad.txt"
        with open("/home/mati/PycharmProjects/FISZKI/documents/" + file_documents) as f:
            list2 = [word.replace(",", "").replace(".", "").replace('"', '').replace("=", "").replace("/", "")
                     for line in f for word in line.split()]  # tworzy listę wyrazów z pliku bez kropek i przecinków

        list3 = [n.lower() for n in list2 if len(n) > 3]
        print("tylko małe litery: ", list3)
        print(len(list3))

        list4 = list(set(list3)) #usuwamy duplikujące się wyrazy
        print("lista bez duplikatów to", len(list4), "słów")

        list5 = [x for x in list3 if x not in know_words]
        print("lista 5 bez znanych", list5)
        print(len(list5))

        word_counts = Counter(list5)  # do zapisania do bazy/ słówka bez liczb
        print("list5", list5)

        top_100 = word_counts.most_common(150)  # już na tym można działać, wyświetlić listę na stronie
        print(top_100)
        return top_100


    def get(self, request):
        top_100 = self.create_flascards()
        ctx = {
            "top_flascards": top_100,
        }
        return render(request, "top_words.html", ctx)



# def save_to_base():
#     for x,y in top_100:
#         a = TopWords(word_eng=x, word_frequency=y)
#         a.save()

# save_to_base()



   #  def create_flascards(self, book_id):
   #      book_title = Document.objects.get(pk=book_id)
   #      print(book_title)
   #      file_documents = book_title
   #
   # def get(self, request, book_id):
   #      top_100 = self.create_flascards()
   #      ctx = {
   #          "top_flascards": top_100,
   #      }
   #      return render(request, "top_words.html", ctx)