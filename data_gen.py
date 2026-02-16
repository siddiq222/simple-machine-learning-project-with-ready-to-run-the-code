from module import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_samples",type=int,required=True,help="This generates data with num_samples")
    parser.add_argument("--file_path",type=str,required=True,help="This is for saving the data")
    args = parser.parse_args()
    num_samples = args.num_samples
    file_path = args.file_path

    gen = data_gen(num_samples,file_path)
    gen.save_data()