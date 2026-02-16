from module import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_path",type=str,required=True,help="Pass the path of generated model")
    args = parser.parse_args()
    model_path = args.model_path
    process = inference(model_path)
    model = process.load_model()
    bio_length = input("please enter your bio :")	
    bio_length = len(bio_length)
    pics_count = int(input("how many pics are you uploading :"))
    print("select one from below :")
    print("enter 1 ----> Fitness")
    print("enter 2 ----> Food")
    print("enter 3 ----> Gaming")
    print("enter 4 ----> Music")
    print("enter 5 ----> Travel")
    print()
    top_interest = int(input("enter your choice :"))
    print("Do you use Spotify ? :")
    print("enter 1 ----> yes")
    print("enter 2 ----> No")
    spotify_connected = int(input("enter your choice :"))
    result = model.predict([[bio_length,pics_count,top_interest,spotify_connected]])[0]
    result = int(result)


    if result == 1:
        print("congratulations") # audio message
        playsound('audio/congratulations.mp3')
    else:
        print("dobbey") # audio message
        playsound('audio/breakup.mp3')