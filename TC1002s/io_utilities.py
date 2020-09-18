import pandas as pd

# io_utilities.py

def readvanilla():

    data = {"S_L":[],"S_W":[],"P_L":[],"P_W":[],"CL":[]}
    filepath = "data/iris.data"
    with open(filepath,"r") as f:
        while (line:=f.readline().strip("\n").split(",")) and len(line) == len(data.keys()):
            for idx,key in enumerate(data.keys()):
                try:
                    data[key].append(float(line[idx]))
                except ValueError as e:
                    data[key].append(line[idx])
    return data


if __name__ == "__main__":
    print(readvanilla())

def read_pandas(filepath,**kwargs):
    
    df = pd.read_csv(filepath,**kwargs)
    return df

if __name__ == "__main__":
    filepath = "data/iris.data"
    df = read_pandas(filepath=filepath,names=["sepal_length","sepal_width","petal_length","petal_width","class"])
    print(df.head())
