# gpt_automation\project_info.py
import os
import gpt_automation.directory_walker

class ProjectInfo:
    def __init__(self, root_dir, black_list=None, white_list=None, profile_names=None):
        self.root_dir = root_dir
        self.black_list = black_list if black_list else []
        self.white_list = white_list if white_list else []
        self.profile_names = profile_names
        self.directory_walker = gpt_automation.directory_walker.DirectoryWalker(
            path=root_dir,
            blacklist=black_list,
            whitelist=white_list,
            profile_names=profile_names
        )

    def create_directory_structure_prompt(self):
        prompt = ""
        for root, dirs, files in self.directory_walker.walk():
            level = root.replace(self.root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            prompt += '{}{}/\n'.format(indent, os.path.basename(root))
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                prompt += '{}{}\n'.format(sub_indent, os.path.basename(file))
        return prompt

    def create_file_contents_prompt(self):
        prompt = ""
        for root, dirs, files in self.directory_walker.walk():
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.root_dir)
                with open(file_path, 'r', encoding='utf-8') as f:
                    prompt += '{}{}:\n'.format('=' * 10, relative_path)
                    prompt += f.read() + '\n\n'
        return prompt
