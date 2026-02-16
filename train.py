from module import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path",type=str,required=True,help="Pass the path of generated data")
    parser.add_argument("--model_save_path",type=str,required=True,help="Pass the path of generated data")
    args = parser.parse_args()
    data_path = args.data_path
    model_save_path = args.model_save_path
    pipe = pipeline(data_path,model_save_path)
    pipe.save_model()