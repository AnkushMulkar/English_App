import streamlit as st

# Dictionary of active voice verb tenses
active_verb_tenses = {
    "V1/v1+e/es": "She writes a letter every day.",
    "Used to+v1": "I used to play the guitar, but I don't anymore.",
    "V2": "He wrote a novel last year.",
    "Had+v3": "They had eaten breakfast before they went to work.",
    "Have/has+v3": "We have seen that movie before.",
    "Was/were+v1ing": "we were providing food to the needy people",
    "Am/is/are+v1ing": "He is playing basketball right now.",
    "Shall/will+v1": "They will go to the beach this weekend.",
    "Would+v1": "I would like to go to the party tonight.",
    "Can+v1": "She can speak French fluently.",
    "Could+v1": "He could run a mile in under six minutes when he was in college.",
    "Could have+v3": "He could have won the competetion",
    "May+v1": "You may come in if you have an appointment.",
    "Might+v1": "He might come this morning for breakfast",
    "Might have": "She might have forgotten her keys at home",
    "Shall+v1": "I shall study regular to make good marks in final exam",
    "Should+v1": "We should start working on the project as soon as possible.",
    "Should have+v3":"we should have worked together for better result",
    "Must+v1": "They must finish their homework before they go out to play.",
    "Must have+v3": "Ministers must have done creative in infra projects",
    "Was/were to+v1": "They were to meet us at the park, but they didn't show up.",
    "Am/is/are to+v1": "She is to meet us at the restaurant in an hour.",
    "Was/were about to+v1": "I was about to leave when my friend called me.",
    "Am/is/are about to+v1": "He is about to take a shower.",
    "Had to+v1": "She had to study for her exams all weekend.",
    "Have/has to+v1": "I have to work late tonight.",
    "Shall/will have to+v1": "They will have to finish the project by tomorrow.",
    "Began to+v1": "She began to sing when the music started.",
    "Begin/begins to+v1": "The class begins to get noisy around this time of day.",
    "Shall/will begin to++v1": "They will begin to work on the project next week.",
    "Had begun to+v1": "I had begun to feel sick before I went to bed.",
    "Have/has begun to+v1": "He has begun to learn how to play the piano.",
    "Shall/will have begun to+v1": "They will have begun to prepare for the exam by the time you arrive.",
    "Remained +v1ing": "They remained seated during the entire performance.",
    "Remin/remains+v1ing": "The baby remains sleeping for most of the afternoon.",
    "Shall/will remain+v1ing": "The statue will remain standing for centuries to come."
}

# Dictionary of passive voice verb tenses

passive_verb_tenses = {
"Am/is/are+v3": "A letter is written by her every day.",
"Used to+be+v3": "The guitar used to be played by me, but not anymore.",
"was/were+v3": "A novel was written by him last year.",
"Had+been+v3": "Breakfast had been eaten by them before they went to work.",
"Have/has+been+v3": "That movie has been seen by us before.",
"Was/were+being": " Cricket was being played by more number of people in india",
"Am/is/are+being": "Basketball is being played by him right now.",
"Shall/will+be+v1": "The beach will be gone to by them this weekend.",
"Would+be+v3": "The party tonight would be liked by me to go to.",
"Would have+be+v3": "If we had taken the earlier flight, we would have been met at the airport by a limousine.",
"Can+be+v3": "French can be spoken fluently by her.",
"Could+be+v3": "A mile in under six minutes could be run by him when he was in college.",
"Could have+been+v3": "The concert could have been enjoyed by more people if it hadn't rained ",
"May+be+v3": "If you have an appointment, you may be allowed to come in.",
"Might+be+v3": "The car might be stolen.",
"Might have+been+v3": "The money might have been stolen",
"Should+be+v3": "The project should be started on as soon as possible by us.",
"Should have+been+v3": "The report should have been submitted yesterday",
"Must+be+v3": "Their homework must be finished before they go out to play.",
"Must have+been+v3": "The package must have been delivered already",
"Was/were to+be+v3": "We were to be met by them at the park, but they didn't show up.",
"Am/is/are to+be+v3": "We are to be met by her at the restaurant in an hour.",
"Was/were about to+be+v3": "I was about to be left when my friend called me.",
"Am/is/are about to+be+v3": "A shower is about to be taken by him.",
"Had to+be+v3": "Her exams had to be studied for all weekend.",
"Have/has to+be+v3": "I have to work late tonight.",
"Shall/will have to+be+v3": "The project will have to be finished by them by tomorrow.",
"Began to+be+v3": "When the music started, singing began to be done by her.",
"Begin/begins to+be+v3": "Around this time of day, the class begins to get noisy.",
"Shall/will begin to+be+v3": "Next week, work on the project will begin to be done by them.",
"Had begun to+be+v3": "Before I went to bed, feeling sick had begun to be felt by me.",
"Have/has begun to+be+v3": "Learning how to play the piano has begun to be done by him.",
"Shall/will have begun to+be+v3": "By the time you arrive, preparing for the exam will have begun to be done by them.",
"Remained to+be": "During the entire performance, being seated remained to be done by them.",
"Remin/remains to+be": "For most of the afternoon, sleeping remains to be done by the baby.",
"Shall/will remain to+be": "For centuries to come, standing will remain to be done by the statue."
}
def main():
    st.title("72 Active Voice & Passive Voive Sentences ")
    
    # Select active or passive voice
    voice = st.selectbox("Voice:", ["Active voice", "Passive voice"], key="voice")

    # Select verb tense based on voice
    if voice == "Active voice":
        verb_tense_key = st.selectbox("Verb tense:", list(active_verb_tenses.keys()), key="verb_tense")
        verb_tense_value = active_verb_tenses[verb_tense_key]
    elif voice == "Passive voice":
        verb_tense_key = st.selectbox("Verb tense:", list(passive_verb_tenses.keys()), key="verb_tense")
        verb_tense_value = passive_verb_tenses[verb_tense_key]
    else:
        st.error("Voice not supported.")
        return
    
    # Display selected verb tense
    st.write("Selected voive & verb :", verb_tense_value)


    
if __name__ == "__main__":
    main()
