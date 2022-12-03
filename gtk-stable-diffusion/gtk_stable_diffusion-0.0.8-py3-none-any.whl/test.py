import os
import toml
if True:
    if True:
        global Path
        from pathlib import Path
        global home
        home = str(Path.home())
        global config_dir
        config_dir = home + "/.config/gtk-stable-diffusion/"
        global config_file_path
        config_file_path = config_dir + "config.toml"
        model_dir = home + "/.cache/huggingface/diffusers/sd-v1-4/"


# Note: We chose TOML because it's commentable (against JSON), simple (against YAML or XML), and non-ambiguous (against INI)
# Although we just implement toml dump as text dump because
# toml.load with toml.TomlPreserveCommentDecoder and toml.dump with toml.TomlPreserveCommentEncoder are completely broken.
        def dump_config(f_path, conf):
            toml_txt =  f"""
# nsfw_filter is for regulating erotics, grotesque, or ... something many normal things. [default=true]
# It's your responsibility to cater to your regulating authority wishes, not by us.
nsfw_filter = {"false" if "nsfw_filter" in conf and not conf["nsfw_filter"] else "true"}

# show_nsfw_filter_toggle is for you who don't want to change the nsfw toggle. [default=true]
show_nsfw_filter_toggle = {"false" if "show_nsfw_filter_toggle" in conf and not conf["show_nsfw_filter_toggle"] else "true"}
"""
            with open(f_path, 'w') as f:
                f.write(toml_txt)

        if not os.path.exists(config_file_path):
            os.makedirs(config_dir, exist_ok=True)
            dump_config(config_file_path, {})

        import toml
        conf = toml.load(config_file_path)
        conf["nsfw_filter"] = False
        dump_config(config_file_path + "_", conf)
