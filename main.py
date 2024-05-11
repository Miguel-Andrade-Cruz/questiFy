import config as cfg
import teacherClass as tch

cfg.insertKey("YOUR_API_KEY")
cfg.MODEL = cfg.chooseModel()


def main():

    roy = tch.Teacher("Roy Sollon", "Filosofia e Sociologia")



    ask = "Liste para mim três grandes filósofos."

    question_wish = roy.requestQuestions("Existencialismo", "3", "descritiva")

    print(question_wish)



if __name__ == "__main__":
    main()
