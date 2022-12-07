from debater_python_api.api.clients.key_point_analysis.KpAnalysisUtils import KpAnalysisUtils
from debater_python_api.api.clients.key_point_analysis.utils import get_all_files_in_dir


def run_on_research_results():
    dirs_with_stances = [
        '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/research/combined',
        '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/research/standalone_questions',
        '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/research/standalone_questions_full_kps_list']
    dirs_no_stances = [
        '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/research/combined/no_stance',
        '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/research/standalone_questions/no_stance',
        '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/research/standalone_questions_full_kps_list/no_stance']
    for dir in dirs_with_stances:
        files = get_all_files_in_dir(dir)
        files = [f for f in files if 'pos.csv' in f or 'neg.csv' in f]
        for f in files:
            KpAnalysisUtils.generate_graphs_and_textual_summary(f, n_top_matches_in_docx=None)
    for dir in dirs_no_stances:
        files = get_all_files_in_dir(dir)
        files = [f for f in files if 'results.csv' in f]
        for f in files:
            KpAnalysisUtils.generate_graphs_and_textual_summary(f, n_top_matches_in_docx=None)


if __name__ == '__main__':
    KpAnalysisUtils.init_logger()

    # run_on_research_results()

    file = '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/temp/eng_kp_input_2022_simplified_multi_kps_con_kpa_results.csv'
    KpAnalysisUtils.generate_graphs_and_textual_summary(file)

    # file = '/Users/yoavkantor/Library/CloudStorage/Box-Box/interview_analysis/debater_p_results/2022/temp/austin_merged_results.csv'
    # KpAnalysisUtils.generate_graphs_and_textual_summary(file)

