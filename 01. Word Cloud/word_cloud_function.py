from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import requests

def word_cloud():
    """
    This function generates simple word cloud, and saves it as .png.
    
    The inputs are: The name of how you want to save the file, 
    and the URL of the text in .txt format (Plain Text - UTF-8).
    
    """

    name = input("Name of the file: ")
    url = input("The URL: ")

    # Book: Metamorphosis by Franz Kafka
    path = requests.get(url)
    text = path.text

    # Remove words.
    stopwords = set(STOPWORDS)
    stopwords.update(["said", "and", "of", "a", "it", "was", "gutenberg", "Project", "tm"])

    # Generates a Word CLoud.
    wordcloud = WordCloud(
        stopwords=stopwords,
        background_color="black",
        width=1600, 
        height=800
    ).generate(text)

    # Display the Image.
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.set_axis_off()

    plt.imshow(wordcloud);
    wordcloud.to_file(name + ".png")


word_cloud()
