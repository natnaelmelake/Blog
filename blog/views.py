from datetime import date
from django.shortcuts import render

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains_resized.jpg",
        "author": "Natnael",
        "date": date(2024, 8, 10),
        "title": "mountain hiking",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
                        And I wasn't even prepared for what happened whilst I was enjoying
                        the view!""",
        "content": """Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
                        To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
                        Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
                        Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
                        Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.""",
    },

     {
        "slug": "Programming is fun",
        "image": "coding.jpg",
        "author": "Natnael",
        "date": date(2024, 8, 3),
        "title": "Programming is great",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
                        And I wasn't even prepared for what happened whilst I was enjoying
                        the view!""",
        "content": """Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
                        To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
                        Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
                        Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
                        Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.""",
    },
    {
        "slug": "Into the woods",
        "image": "woods.jpg",
        "author": "Natnael",
        "date": date(2024, 8, 5),
        "title": "NATURE AT IT'S BEST",
        "excerpt": """There's nothing like the views you get when hiking in the mountains!
                        And I wasn't even prepared for what happened whilst I was enjoying
                        the view!""",
        "content": """Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the embed code for the video you want to add. You can also type a keyword to search online for the video that best fits your document.
                        To make your document look professionally produced, Word provides header, footer, cover page, and text box designs that complement each other. For example, you can add a matching cover page, header, and sidebar. Click Insert and then choose the elements you want from the different galleries.
                        Themes and styles also help keep your document coordinated. When you click Design and choose a new Theme, the pictures, charts, and SmartArt graphics change to match your new theme. When you apply styles, your headings change to match the new theme.
                        Save time in Word with new buttons that show up where you need them. To change the way a picture fits in your document, click it and a button for layout options appears next to it. When you work on a table, click where you want to add a row or a column, and then click the plus sign.
                        Reading is easier, too, in the new Reading view. You can collapse parts of the document and focus on the text you want. If you need to stop reading before you reach the end, Word remembers where you left off - even on another device.""",
    }
]


def get_date(post):
    return post.get("date")

# Create your views here.

def starting_page(request):
    sorted_list=sorted(all_posts,key=get_date)
    latest_post=sorted_list[-3:]
    return render(request, "blog/index.html",{
        "posts":latest_post
    })


def posts(request):
    return render(request, "blog/all-posts.html",{
        "all_posts":all_posts
    })


def post_details(request, slug):
    identified_post=next(post for post in all_posts if post['slug']==slug)
    return render(request, "blog/post-detail.html",{
        "post":identified_post
    })


