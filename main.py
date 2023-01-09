"""
This program tests the reaction time of students of different sexes and ages from 12-18.
As well as provides the user with an option to view a leaderboard with the best times and the ability to see
each age's slowest, fastest and average reaction time.

Stephan Tinel
"""

from guizero import App, Text, Box, Picture, Window, TextBox, Combo, ButtonGroup
import random
import datetime


info = []


def title(master,text,screen):
    #this function creates a title at the top if a window

    global title_box
    global button_box

    top_margin = Box(master, width = "fill", height = 30)
    title_box = Box(master, width = "fill", height = 250)

    if screen == "leaderboard":
        button_box = Box(title_box, align = "left", width = 230, height = "fill")
        title = Text(title_box, text = text, size = 150, font = "Baloo 2", align = "left")

    else:
        title = Text(title_box, text = text, size = 150, font = "Baloo 2")




def menu():
    #this function creates a menu for the application

    global app

    title(app,"REACTION TIME","app")
    button_box = Box(app, width = 1000, height = 800)

    play_button = Picture(button_box, image = "Play_Button_DD.png", width = 283, height = 213)
    play_button.when_clicked = play1

    leaderboard_button = Picture(button_box, image = "Leaderboard_Button_DD.png", width = 283, height = 213)
    leaderboard_button.when_clicked = leaderboard

    data_button = Picture(button_box, image = "Data_Button_DD copy.png", width = 283, height = 213)
    data_button.when_clicked = data





def play1():
    #This function creates a window which gathers the user's data

    global app
    global play1_window
    global input_name
    global input_age
    global input_sex

    app.hide()

    play1_window = Window(app, title= "Reaction Time", bg ="#FA7500")
    title(play1_window,"REACTION TIME","play1")

    #creates layout boxes
    center_up_box = Box(play1_window, height = "150", width = 600)
    center_down_box = Box(play1_window, height = "150", width = 600)
    name_subtitle = Text(center_up_box, text = "NAME: ", size = 50, align = "left", font = "Baloo 2")

    #allows for input of name
    input_name = TextBox(center_up_box, text="", width = 20, align = "left" )
    input_name.text_size = 30
    input_name.text_color = "black"
    input_name.font = "Baloo 2"

    #allows for input of age
    age_subtitle = Text(center_down_box, text = "AGE: ", size = 50, align = "left", font = "Baloo 2")
    input_age = Combo(center_down_box, options=[12, 13, 14, 15, 16, 17, 18] , align = "left", )
    input_age.text_color = "black"
    input_age.font = "Baloo 2"
    input_age.text_size = 50

    split_box = Box(center_down_box, height = "fill", width = 150, align = "left")

    #allows for input of sex
    sex_subtitle = Text(center_down_box, text = "SEX: ", size = 50, align = "left", font = "Baloo 2")
    input_sex = ButtonGroup(center_down_box, options=["Male", "Female"] , align = "left", )
    input_sex.text_color = "black"
    input_sex.font = "Baloo 2"
    input_sex.text_size = 30

    button_split_box = Box(play1_window, height = "75", width = "fill")

    #creates a button which when pressed takes the user to the next stage of the app
    done_button = Picture(play1_window, image = "Done_Button.png", width = 283, height = 213)
    done_button.when_clicked = play2




def play2():
    #this function provides instructions to the reaction time test

    global play2_window
    global play1_window
    global user_info
    global input_name
    global input_age
    global input_sex

    user_info = [input_name.value, input_age.value, input_sex.value]

    play1_window.hide()
    play2_window = Window(app, title= "Reaction Time", bg ="#FA7500")
    play2_window.set_full_screen()
    play1_window.destroy()
    title(play2_window,"REACTION TIME","play2")

    instruction_box = Box(play2_window, width = 900, height = 350)
    instruction_title_box = Box(instruction_box, width = "fill" , height = 100,)

    #displays the instructions
    instructions_title = Text(instruction_title_box, text = "Instructions:", size = 60, align = "left")

    instruction_box1 = Box(instruction_box, width = "fill", height = 50)
    instruction_box2 = Box(instruction_box, width = "fill", height = 50)
    instruction_box3 = Box(instruction_box, width = "fill", height = 50)
    instruction_box4 = Box(instruction_box, width = "fill", height = 50)

    instructions = Text(instruction_box1, text = "Once a color at the top appears, press the colored", size = 40, align = "left")
    instructions = Text(instruction_box2, text = "box that corresponds to it as fast as possible.", size = 40, align = "left")
    instructions = Text(instruction_box3, text = "This process will repeat five times. If the colors", size = 40, align = "left")
    instructions = Text(instruction_box4, text = "do not match you will get anther try.", size = 40, align = "left")

    #creates a button which when pressed takes the user to the next stage of the app
    ready_button = Picture(play2_window, image = "Ready_Button_DD.png", width = 424, height = 319)
    ready_button.when_clicked = play3




def play3():
    #This function tests the user's reaction time

    global play2_window
    global random_box
    global random_color
    global count
    global play3_window
    global rectangle_green_box
    global rectangle_blue_box
    global rectangle_orange_box
    global rectangle_red_box
    global countdown_number
    global trials

    trials = 0
    random_color = False

    play2_window.hide()
    play3_window = Window(app, title= "Reaction Time", bg ="#008FAD")
    play2_window.destroy()

    #display of the countdown
    top_box = Box(play3_window, width = "fill" , height = 300)
    random_box = Box(top_box, width = 400, height = 200)
    countdown_number = Text(random_box, text = "3", size = 200)
    count = 3
    countdown()

    #display of the colors to be pressed
    colors_box = Box(play3_window, width = "fill" , height = 600)
    top_colors_box = Box(colors_box, width = "fill" , height = 290)
    margin_top_left = Box(top_colors_box, width = 10, height = "fill", align = "left")
    rectangle_green_box = Box(top_colors_box, width = 700, height = "fill", align = "left")
    rectangle_green_box.bg = "green"
    margin_green_blue_box = Box(top_colors_box, width = 20, height = "fill", align = "left")
    rectangle_blue_box = Box(top_colors_box, width = 700, height = "fill", align = "left")
    rectangle_blue_box.bg = "blue"

    margin_top_bottom_box = Box(colors_box, width = "fill" , height = 20)

    bottom_colors_box = Box(colors_box, width = "fill" , height = 280)
    margin_bottom_left = Box(bottom_colors_box, width = 10, height = "fill", align = "left")
    rectangle_orange_box = Box(bottom_colors_box, width = 700, height = "fill", align = "left")
    rectangle_orange_box.bg = "orange"
    margin_orange_red_box = Box(bottom_colors_box, width = 20, height = "fill", align = "left")
    rectangle_red_box = Box(bottom_colors_box, width = 700, height = "fill", align = "left")
    rectangle_red_box.bg = "red"

    press()




def press():
    #this function runs a command when one of the colors are clicked
    global rectangle_green_box
    global rectangle_blue_box
    global rectangle_orange_box
    global rectangle_red_box

    rectangle_green_box.when_clicked = time_calculation
    rectangle_blue_box.when_clicked = time_calculation
    rectangle_orange_box.when_clicked = time_calculation
    rectangle_red_box.when_clicked = time_calculation




def time_calculation(event):
    #this calculates the reaction time of the user on each trial

    global color_display_time_str
    global random_box
    global random_color
    global user_info
    global trials
    global countdown_number


    random_box.bg = "#008FAD"

    if event.widget.bg == random_color:

        random_color = False

        #finds the time at which the user clicked the color
        color_pick_time = datetime.datetime.now()
        color_pick_time_str = color_pick_time.strftime("%M:%S:%f")

        #converts first press time to a clear format
        first_list = list(color_display_time_str)
        first_list_accurate = str(int(first_list [0] + first_list [1])*60 + int(first_list [3] + first_list [4])) + first_list [6] + first_list [7] + first_list [8] + first_list [9] + first_list [10] + first_list [11]

        #converts second press time to a clear format
        second_list = list(color_pick_time_str)
        second_list_accurate = str(int(second_list [0] + second_list [1])*60 + int(second_list [3] + second_list [4])) + second_list [6] + second_list [7] + second_list [8] + second_list [9] + second_list [10] + second_list [11]

        #finds the difference between the times
        dif_time = (abs(int(second_list_accurate) - int(first_list_accurate)))
        time = str(int(round(dif_time,-3) / 1000))
        user_info.append(int(time))

        trials += 1

        if trials < 5:
            #restarts a new trial
            countdown_number.show()
            random_box.after(random.randint(3000,8000),random_color_display)

    elif random_color == False:
        #notifies the user that they clicked a color too early and resets the trial
        random_box.cancel(random_color_display)
        countdown_number.value = "Too Early"
        countdown_number.text_size = 60
        random_box.after(2000,hide)
        countdown_number.show()

    else:
        #notifies the user that they pressed the wrong color and resets the trial
        random_color = False
        random_box.cancel(random_color_display)
        countdown_number.value = "Wrong Color"
        countdown_number.text_size = 60
        random_box.after(2000,hide)
        countdown_number.show()

    if trials == 5:
        results()




def hide():
    #this function resets a reaction time trial

    global countdown_number
    global random_box

    countdown_number.value = "..."
    countdown_number.text_size = 200
    random_box.after(random.randint(3000,8000),random_color_display)




def countdown():
    #this function counts down from three

    global count
    global countdown_number

    countdown_number.value = count

    count -= 1
    if count == 2:
        random_box.after(1000, countdown)
    elif count == 1:
        random_box.after(1000, countdown)
    elif count == 0:
        random_box.after(1000, countdown)
    elif count == -1 :
        countdown_number.value = "..."
        random_box.after(random.randint(2000,8000),random_color_display)



def random_color_display():
    #this function displays a random color (green/blue/orange/red)

    global play3_window
    global random_color
    global color_display_time_str

    countdown_number.hide()

    #random color
    random_number = random.randint(1,4)
    if random_number == 1:
        random_color = "green"
    elif random_number == 2:
        random_color = "blue"
    elif random_number == 3:
        random_color = "orange"
    elif random_number == 4:
        random_color = "red"

    top_box = Box(play3_window, width = "fill" , height = 300)
    top_margin = Box(top_box, width = "fill" , height = 50)

    #display random color and stores time
    random_box.bg = random_color
    color_display_time = datetime.datetime.now()
    color_display_time_str = color_display_time.strftime("%M:%S:%f")

    press()




def results():
    #this function displays the user's results

    global play3_window
    global results_window
    global user_info

    play3_window.hide()
    results_window = Window(app, title= "Reaction Time", bg ="#008FAD")
    results_window.set_full_screen()
    play3_window.destroy()
    title(results_window,"RESULTS","results")

    left_margin_box = Box(results_window, width = 75 , height = "fill", align = "left")
    times_box = Box(results_window, width = 500 , height = "fill", align = "left")

    #finds each of the user's times
    first_time = "1.      " + str(user_info[3]) + "  ms"
    second_time = "2.      " + str(user_info[4]) + "  ms"
    third_time = "3.      " + str(user_info[5]) + "  ms"
    fourth_time = "4.      " + str(user_info[6]) + "  ms"
    fifth_time = "5.      " + str(user_info[7]) + "  ms"

    #calculates average time
    average_time = (user_info[3] + user_info[4] + user_info[5] + user_info[6] + user_info[7]) / 5
    user_info.append(average_time)

    #displays each of the user's times
    first_time_text = Text(times_box,text = first_time , font = "Baloo 2", size = 75,)
    second_time_text = Text(times_box,text = second_time , font = "Baloo 2", size = 75)
    third_time_text = Text(times_box,text = third_time , font = "Baloo 2", size = 75)
    fourth_time_text = Text(times_box,text = fourth_time , font = "Baloo 2", size = 75)
    fifth_time_text = Text(times_box,text = fifth_time , font = "Baloo 2", size = 75)

    #displays the user's average time
    average_text = Text(results_window,text = "Average" , font = "Baloo 2", size = 110)
    average_time_text = Text(results_window,text = str(average_time) + "  ms" , font = "Baloo 2", size = 75)

    split_box = Box (results_window, width = "fill", height = 40)

    #creates a button which when pressed takes the user back to the menu
    menu_button = Picture(results_window, image = "Menu_Button_DD copy.png", width = 424, height = 319)
    menu_button.when_clicked = go_back




def leaderboard():
    #this function creates a leaderboard of the top 5 reaction times

    global app
    global button_box
    global leaderboard_window

    app.hide()
    leaderboard_window = Window(app, title= "Reaction Time", bg ="#00A2F5")
    title(leaderboard_window,"LEADERBOARD","leaderboard")

    #creates a button which when pressed takes the user back to the menu
    menu_button = Picture(button_box, image = "Menu_Button_DD copy.png", width = 212, height = 160)
    menu_button.when_clicked = go_back

    #finds the 5 users with the fastest reaction time and displays them in order of fastest to slowest
    leaderboard_box = Box(leaderboard_window, width = 900, height = 600)
    leaderboard_box.bg = "#FA7500"

    info_dif = info.copy()

    if len(info) >= 1:
        first = fastest(info)
        first_place_time = first[8]
        first_place_name = first[0]
        first_place_age = first[1]
        first_place_box = Box(leaderboard_box, width = "fill", height = 100)
        first_place_text = Text(first_place_box,text = "#1  " + first_place_name + "   Time  " + str(first_place_time) + "  ms    Age  " + str(first_place_age), size = 50, align = "left", font = "Baloo 2")
        margin1_box = Box(leaderboard_box, width = "fill", height = 25)

        info_dif.remove(first)

    if len(info) >= 2:
        second = fastest(info_dif)
        second_place_time = second[8]
        second_place_name = second[0]
        second_place_age = second[1]
        second_place_box = Box(leaderboard_box, width = "fill", height = 100)
        second_place_text = Text(second_place_box,text = "#2  " + second_place_name + "   Time  " + str(second_place_time) + "  ms    Age  " + str(second_place_age), size = 50, align = "left", font = "Baloo 2")
        margin2_box = Box(leaderboard_box, width = "fill", height = 25)

        info_dif.remove(second)

    if len(info) >= 3:
        third = fastest(info_dif)
        third_place_time = third[8]
        third_place_name = third[0]
        third_place_age = third[1]
        third_place_box = Box(leaderboard_box, width = "fill", height = 100)
        third_place_text = Text(third_place_box,text = "#3  " + third_place_name + "   Time  " + str(third_place_time) + "  ms    Age  " + str(third_place_age), size = 50, align = "left", font = "Baloo 2")
        margin3_box = Box(leaderboard_box, width = "fill", height = 25)

        info_dif.remove(third)

    if len(info) >= 4:
        fourth = fastest(info_dif)
        fourth_place_time = fourth[8]
        fourth_place_name = fourth[0]
        fourth_place_age = fourth[1]
        fourth_place_box = Box(leaderboard_box, width = "fill", height = 100)
        fourth_place_text = Text(fourth_place_box,text = "#4  " + fourth_place_name + "   Time  " + str(fourth_place_time) + "  ms    Age  " + str(fourth_place_age), size = 50, align = "left", font = "Baloo 2")
        margin4_box = Box(leaderboard_box, width = "fill", height = 25)

        info_dif.remove(fourth)

    if len(info) >= 5:
        fifth = fastest(info_dif)
        fifth_place_time = fifth[8]
        fifth_place_name = fifth[0]
        fifth_place_age = fifth[1]
        fifth_place_box = Box(leaderboard_box, width = "fill", height = 100)
        fifth_place_text = Text(fifth_place_box,text = "#5  " + fifth_place_name + "   Time  " + str(fifth_place_time) + "  ms    Age  " + str(fifth_place_age), size = 50, align = "left", font = "Baloo 2")

    if len(info) == 0:
        #tells the user there is no data if there are no reaction times tested
        no_data = Text(leaderboard_box, text = "No Data", size = 100 , font = "Baloo 2")





def fastest(info):
    #this function finds the fastest time of a sample of users

    fastest = info[0]
    for i in range(len(info)):

        if info [i][8] < fastest [8]:
            fastest = info [i]
    return fastest




def go_back(event):
    #this function returns the user to the app menu

    global results_window
    global leaderboard_window
    global button_box
    global app
    global info
    global user_info
    global data_window

    app.show()
    if event.widget.master == results_window:
        results_window.destroy()
        info.append(user_info)

    elif event.widget.master == button_box:
        leaderboard_window.destroy()

    elif event.widget.master == data_window:
        data_window.destroy()




def data():
    #this function allows the user to input an age and see the slowest, fastest and average reaction time of that age

    global app
    global input_age
    global data_window
    global slowest_text
    global average_text
    global fastest_text


    app.hide()
    data_window = Window(app, title= "Reaction Time", bg = "#FA7500")
    title(data_window,"DATA","data")

    #allows the user to input an age
    age_box = Box (data_window, width = 700, height = 100)
    input_age = TextBox(age_box, text="Enter Age", width = 15, align = "left")
    margin_button_box = Box (age_box, width = 60, height = "fill", align = "left")
    input_age.text_size = 40
    input_age.text_color = "black"
    input_age.font = "Baloo 2"
    enter_button = Picture(age_box, image = "Enter_Button.png", width = 212, height = 160)

    #layout
    margin_box = Box (data_window, width = "fill", height = "80")
    middle_box = Box(data_window, width = 1300, height = 250)
    left_box = Box(middle_box, width = 400, height = "fill", align = "left")
    margin1_box = Box(middle_box, width = 33, height = "fill", align = "left")
    center_box = Box(middle_box, width = 400, height = "fill", align = "left")
    margin2_box = Box(middle_box, width = 33, height = "fill", align = "left")
    right_box = Box(middle_box, width = 400, height = "fill", align = "left")

    #displays the slowest,fastest and average time
    slowest_subtitle = Text(left_box, text = "Slowest", size = 50, font = "Baloo 2")
    average_subtitle = Text(center_box, text = "Average", size = 50, font = "Baloo 2")
    fastest_subtitle = Text(right_box, text = "Fastest", size = 50, font = "Baloo 2")
    slowest_text = Text(left_box, text = ".   .   .", size = 80, font = "Baloo 2")
    average_text = Text(center_box, text = ".   .   .", size = 80, font = "Baloo 2")
    fastest_text = Text(right_box, text = ".   .   .", size = 80, font = "Baloo 2")

    #finds the data once enter button is pressed
    enter_button.when_clicked = data_calculations

    #creates a button which when pressed takes the user back to the menu
    menu_button = Picture(data_window, image = "Menu_Button_DD copy.png", width = 339, height = 255)
    menu_button.when_clicked = go_back




def data_calculations():
    #calculates the slowest,fastest and average reaction times of a specific age of users

    global input_age
    global info
    global slowest_text
    global average_text
    global fastest_text

    dif_info = []

    #creates a list with all the users of the corresponding age
    for i in range(len(info)):
        if info [i][1] == input_age.value:
            dif_info.append(info [i])

    #calculates the slowest reaction time
    slowest = dif_info [0][8]
    for i in range(len(dif_info)):
        if dif_info [i][8] > slowest:
            slowest = dif_info [i][8]

    #calculates the fastest reaction time
    fastest = dif_info [0][8]
    for i in range(len(dif_info)):
        if dif_info [i][8] < fastest:
            fastest = dif_info [i][8]

    #calculates the average reaction time
    sum = 0
    for i in range(len(dif_info)):
        sum += dif_info [i][8]

    average = round(sum / len(dif_info),1)

    #returns the slowest,fastest and average reaction time
    slowest_text.value = slowest
    average_text.value = average
    fastest_text.value = fastest



app = App(title= "Reaction Time", bg ="#008FAD")
menu()
app.display()

