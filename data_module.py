import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img_a = mpimg.imread('Screen_time_by_app.png')
img_b = mpimg.imread('phone_anxiety_pie_chart.png')
img_c = mpimg.imread('sleep_issue_pie_chart.png')
img_d = mpimg.imread('constantly_online_pie_chart.png')

df_a = pd.read_csv('Teens&Screens_data.csv')
df_b = pd.read_csv('platform_analysis_20250808_134948.csv')
df_c = pd.read_csv('age_group_analysis_20250808_134948.csv')

def display_dataset_preview():
    while True:
        print("\n=== Dataset Preview Interface ===")
        print("1. Teens & Screens analysis")
        print("2. Platform analysis")
        print("3. Age Group analysis")
        print("4. Back to main menu")

        dataset = input("Choose Dataset 1-4: ").strip()
        if dataset == '1':
            print(df_a)
        elif dataset == '2':
            print(df_b)
        elif dataset == '3':
            print(df_c)
        elif dataset == '4':
            break
        else:
            print("Please choose a valid option from 1-4")

    pass

def display_visualisation():
    while True:
        print("\n=== Dataset Visualisation Interface ===")
        print("1. Screen Time Chart")
        print("2. Phone Anxiety Chart")
        print("3. Sleep Issue Chart")
        print("4. Constantly Online Chart")
        print("5. Back to main menu")

        dataset = input("Choose Chart 1-5: ").strip()
        if dataset == '1':
            plt.imshow(img_a)
            plt.axis('off')
            plt.show()
        elif dataset == '2':
            plt.imshow(img_b)
            plt.axis('off')
            plt.show()
        elif dataset == '3':
            plt.imshow(img_c)
            plt.axis('off')
            plt.show()
        elif dataset == '4':
            plt.imshow(img_d)
            plt.axis('off')
            plt.show()
        elif dataset == '5':
            break
        else:
            print("Please choose a valid option from 1-5")

def search_data():
    while True:
        print("\n=== Dataset Preview Interface ===")
        print("1. Teens & Screens dataset")
        print("2. Platform dataset")
        print("3. Age Group dataset")
        print("4. Back to main menu")

        dataset = input("Choose Dataset 1-4: ").strip()
        if dataset == '1':
            row = input("Choose the row:")
            if row > '1203':
                print("Please choose a smaller number")
            elif row <= '1203':
                integer_row = int(row)
                print(df_a.iloc[integer_row])
            else:
                print("Input a number from 1-1203")
        elif dataset == '2':
            row = input("Choose the row:")
            if row > '6':
                print("Please choose a smaller number")
            elif row <= '6':
                integer_row = int(row)
                print(df_b.iloc[integer_row])
            else:
                print("Input a number from 1-6")
        elif dataset == '3':
            row = input("Choose the row:")
            if row > '5':
                print("Please choose a smaller number")
            elif row <= '5':
                integer_row = int(row)
                print(df_c.iloc[integer_row])
            else:
                print("Input a number from 1-5")
        elif dataset == '4':
            break
        else:
            print("Please choose a valid option from 1-4")
    pass
