import config as cfg
import teacherClass as tch

cfg.insertKey("YOUR_API_KEY_HERE")
cfg.MODEL = cfg.chooseModel()


def main():

    roy = tch.Teacher("Roy Sollon", "Filosofia e Sociologia")



    ask = "Liste para mim três grandes filósofos."

    response = roy.simpleAsk(ask)

    print(response)



if __name__ == "__main__":
    main()
