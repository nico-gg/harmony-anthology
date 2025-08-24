import os
import pandas as pd

def make_file_name(author, work, measure):
    return '-'.join(['_'.join(author.split()), 
                      "_".join(work.split() + measure.split())])


examples_df = pd.read_csv("tooling\\\\examples.csv", index_col=False)

for i, folder, author, work, measure, text in examples_df.itertuples():
    image_name = make_file_name(author, work, measure)
    full_path = f"images\\\\{folder}\\\\{image_name}.png"

    try: 
        os.rename(f"tooling\\\\example_images\\\\{i}.png", full_path)
    except FileExistsError:
        print(f"could not write {full_path}")
    except FileNotFoundError:
        print(f"could not find image {i}.png")

    online_path = "../" + full_path.replace('\\\\', '/')
    with open("tooling\\\\examples_output.md", "a") as f:
        f.write(f"# {folder} \n\n")
        f.write(f"- **{author}, {work} {measure}:** {text} \n\n")
        f.write(f"  ![]({online_path}) \n\n")
