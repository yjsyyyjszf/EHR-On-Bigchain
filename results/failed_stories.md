## happy path 1
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: thank: amazing -->
    - utter_happy   <!-- predicted: utter_thank -->


## happy path 2
* greet: hello there!
    - utter_greet
* mood_great: amazing   <!-- predicted: thank: amazing -->
    - utter_happy   <!-- predicted: utter_thank -->
* goodbye: bye-bye!   <!-- predicted: bye: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_bye -->


## sad path 1
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: bye: not good -->
    - utter_cheer_up   <!-- predicted: utter_bye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_bye -->
* affirm: yes   <!-- predicted: greet: yes -->
    - utter_happy   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_greet -->


## sad path 2
* greet: hello
    - utter_greet
* mood_unhappy: not good   <!-- predicted: bye: not good -->
    - utter_cheer_up   <!-- predicted: utter_bye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_bye -->
* deny: not really   <!-- predicted: greet: not really -->
    - utter_goodbye   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_greet -->


## sad path 3
* greet: hi
    - utter_greet
* mood_unhappy: very terrible   <!-- predicted: bye: very terrible -->
    - utter_cheer_up   <!-- predicted: utter_bye -->
    - utter_did_that_help   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_bye -->
* deny: no   <!-- predicted: bye: no -->
    - utter_goodbye   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_bye -->


## say goodbye
* goodbye: bye-bye!   <!-- predicted: bye: bye-bye! -->
    - utter_goodbye   <!-- predicted: utter_bye -->


## bot challenge
* bot_challenge: are you a bot?   <!-- predicted: greet: are you a bot? -->
    - utter_iamabot   <!-- predicted: utter_greet -->


