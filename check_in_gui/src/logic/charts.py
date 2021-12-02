import matplotlib.pyplot as plt
from utils.config import IMAGES_PATH

def generate_pie_check_in_percentage(stat_list):
    labels = 'Made it', "Missed"
    missed_count = 0
    made_it_count = 0
    for stat in stat_list:
        if stat.checked_in_on_time == True:
            made_it_count+=1
        else:
            missed_count+=1
    sizes = [made_it_count/len(stat_list), missed_count/len(stat_list)]
    colors = ["green","red"]
    patches, texts, _ = plt.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90, colors=colors)
    plt.legend(patches, labels,loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(IMAGES_PATH+"/pie.png")
