## Basic workflow in dvc in this project.

1. First created git repo with name simple-dvc-project, added gnu licence.
2. clone it to your local machine.
3. in your simple-dvc-project, create following structure.
4. src/utils, artifacts/.geetkeep, setup.py, src/__init__.py, dvc.yaml.

5. Now some files in src. like src/[stage_01_load_and_save.py, stage_02_split_data.py, .....].

6. fill setup.py file as we have done.

7. now we installed the requirements mentioned in requirements.txt file using command

```bash
pip install -r requirements.txt
```

8. initialize dvc

```bash
dvc init
```

9. after that we filled param.yaml file, behaves like key-value pair.

10. now complete stage_01 file.

11. also complete common utility functions like loading and getting_data, etc.

12. complete dvc.yaml file, it contains stages in dvc pipline and commands needed to execute them.

13. eg. ```bash
python src/stage_01_load_and_save.py" --config=params.yaml ```

14. complete the dvc.yaml file and now we can use this file to run stages. To do so, do 

```bash
dvc repro
```
15. Above line will produce a file called dvc.lock containg info about stages.




We already know how to create dvc, project. For reference, see <a href="https://github.com/astrovishalthakur/AIOPS">github.</a>

Now when all files are created, as we made in this project, we need to 