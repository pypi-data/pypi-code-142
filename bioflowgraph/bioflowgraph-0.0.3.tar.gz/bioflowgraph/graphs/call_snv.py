# coding=utf-8
from typing import List, Callable
from exuse.exlogging import init_logging
from bioflowgraph import Task, MultiSampleTaskGraph, FragmentedSampleListReader

GetIndexFn = Callable[[str], int]
GetMergeFn = Callable[[str], str]

init_logging()


class SnvCallingTaskGraph(MultiSampleTaskGraph):

    # 将工具函数声明为实例方法以支持 pickle
    def get_annovar_op(self, fp):
        # annovar 的 op port 是一个文件名前缀
        return f'{fp}.hg38_multianno.txt'

    # override
    def define_graph(self, **kwargs):
        # 需要 **kwargs 接收其他不需要的参数，否则函数调用失败
        sample_list_file = kwargs.get('sample_list_file')
        rd = FragmentedSampleListReader(sample_list_file)

        annovars: List[Task] = []
        for patient, patientd in rd.grouped_samples.items():
            td = patientd['tumor']
            nd = patientd['normal']
            t_name = td['sample']  # tumor sample name
            n_name = nd['sample']  # normal sample name
            teps = {'Tumor': t_name, 'Normal': n_name}

            bwa_t = self.add_bwa(t_name, rd.get_fqs(patient, 'tumor', 1), rd.get_fqs(patient, 'tumor', 2))
            bwa_n = self.add_bwa(n_name, rd.get_fqs(patient, 'normal', 1), rd.get_fqs(patient, 'normal', 2))

            md_t = self.add_task(t_name, 'markdup', bwa_t)
            md_n = self.add_task(n_name, 'markdup', bwa_n)

            break

            sb_t = self.add_task(t_name, 'sortbam', {'input_file': (md_t, 'output_file')})
            sb_n = self.add_task(n_name, 'sortbam', {'input_file': (md_n, 'output_file')})

            mutect2 = self.add_task(patient, 'mutect2', {'input_files': [sb_t, sb_n]}, teps)

            lrom = self.add_task(patient, 'LearnReadOrientationModel', (mutect2, 'f1r2_file'), teps)

            t_gps = self.add_task(t_name, 'GetPileupSummaries', {'input_files': sb_t})
            n_gps = self.add_task(n_name, 'GetPileupSummaries', {'input_files': sb_n})

            _ = {'input_table': t_gps, 'matched_normal_input_table': n_gps}
            cc = self.add_task(patient, 'CalculateContamination', _, teps)

            _ = {
                'contamination_table_file': cc,
                'ob_priors': lrom,
                'variant_vcf_file': (mutect2, 'variant_file')
            }
            fmc = self.add_task(patient, 'FilterMutectCalls', _, teps)

            annovar = self.add_task(patient, 'annovar', {'variant_vcf_file': fmc}, teps)

            annovars.append(annovar)

        # targets = [(t, 'output_prefix', self.get_annovar_op) for t in annovars]
        # cat = self.add_task('total', 'cat', {'targets': targets})


ExportedGraph = SnvCallingTaskGraph
