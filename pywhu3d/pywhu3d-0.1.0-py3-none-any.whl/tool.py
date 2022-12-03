import ntpath

import numpy as np
import os, h5py, sys
import open3d as o3d
from laspy.file import File
import plyfile as ply

from rich.console import Console
console = Console(soft_wrap=True)
print = console.print
input = console.input
rule = Console(soft_wrap=True, width=100).rule
from rich.progress import track
from rich.table import Column, Table
from rich.text import Text
import json
from rich.progress import Progress
pprint = Progress().console.print
# from configs.mls_config_pole import MLSInsConfig as Config, sem_list_no_ins, sem_map, class2label, raw_class_label, sem_color_map


def newpath(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:
        yn = input('[red]h5 folder already exists, still process (\[y]/n)?')
        if yn == 'n':
            return False
        else:
            return True


class WHU3D:
    def __init__(self,  data_root, data_type, format, scenes=[]):
        '''
        data_root: where is the data
        data_type: als, mls, image
        format: txt, ply, npy, h5, pickle
        [optional] scenes: a list of scenes
        '''
        self.data_root = data_root
        self.data_path = os.path.join(data_root, data_type)
        self.data_type = data_type
        self.format = format
        self.scenes = scenes
        self.data = {}
        self.labels = {}
        self.gt = {}
        if format == 'txt':
            self.load_txt(os.path.join(data_root, data_type, 'txt'))
        elif format == 'h5':
            self.load_h5(os.path.join(data_root, data_type, 'h5'))

        if data_type == 'mls':
            from pywhu3d.configs.mls_config_pole import sem_list_no_ins, sem_map, raw_label_class, seg_label_to_cat_en, compute_ins_list, train_split, test_split, val_split
        elif data_type == 'als':
            from pywhu3d.configs.als_config import sem_list_no_ins, sem_map

        self.sem_list_no_ins = sem_list_no_ins
        self.sem_map = sem_map
        self.label2cat = raw_label_class
        self.gt2cat = seg_label_to_cat_en
        self.num_classes = len(self.gt2cat)
        self.compute_ins_list = compute_ins_list
        self.train_split = train_split
        self.test_split = test_split
        self.val_split = val_split

        print('Num of scenes: %d' % len(self.scenes))

    def load_txt(self, input):
        flist = os.listdir(input)
        load_scenes = [scene.split('.')[0] for scene in flist] if len(self.scenes) == 0 else self.scenes
        self.scenes = []
        for scene in track(load_scenes, description='[cyan]loading txt data...'):
            pprint('processing %s...' % scene)
            points = np.loadtxt(os.path.join(input, scene + '.txt'), delimiter=' ')
            if points.shape[-1] == 11:
                x, y, z, a, b, intensity, sem, ins, r, g, b = np.split(points, points.shape[1], axis=1)
                return_num = a if a.max() == 3 else b
                # pprint('[grey]#return: %.1f, time: %.1f, intensity: %.1f' % (return_num.max(), pts_time.max(), intensity.max()))
            elif points.shape[-1] == 12:
                x, y, z, edge, return_num, pts_time, intensity, sem, ins, r, g, b = np.split(points, points.shape[1], axis=1)
                # pprint('[grey]#edge: %.1f, #return: %.1f, time: %.1f, intensity: %.1f' % (edge.max(), return_num.max(), pts_time.max(), intensity.max()))
            else:
                pprint('[orange1][Warning: loaded features number wrong!] passing %s' % scene)
                continue
            pprint('[bright_black]#return: %.1f, intensity: %.1f' % (return_num.max(), intensity.max()))
            self.data[scene] = {}
            self.labels[scene] = {}
            self.data[scene]['coords'] = np.concatenate([x, y, z], axis=-1)
            self.labels[scene]['semantics'] = sem.squeeze()
            self.labels[scene]['instances'] = ins.squeeze()
            self.data[scene]['number_returns'] = return_num.squeeze()
            self.data[scene]['intensity'] = intensity.squeeze()
            self.scenes.append(scene)

    def load_h5(self, input):
        flist = os.listdir(input)
        if len(self.scenes) == 0:
            self.scenes = [scene.split('.')[0] for scene in flist]
        for scene in track(self.scenes, description='[cyan]loading h5 data...'):
            pprint('processing %s...' % scene)
            fin = h5py.File(os.path.join(input, scene + '.h5'), 'r')
            self.data[scene] = {}
            self.labels[scene] = {}
            self.data[scene]['coords'] = fin['coords'][:]
            self.labels[scene]['semantics'] = fin['semantics'][:]
            self.labels[scene]['instances'] = fin['instances'][:]
            self.data[scene]['number_returns'] = fin['number_returns'][:]
            # self.data[scene]['edge_flight_line'] = fin['edge_flight_line'][:]
            self.data[scene]['intensity'] = fin['intensity'][:]

    def export_las(self):
        pass

    def export_label(self):
        pass

    def export_ply(self):
        attrs = self.list_attributes(False)
        attrs = [at.split('/')[-1] for at in attrs]
        at_set = set(attrs)


    def export_h5(self, output_dir='', scenes=[]):
        if output_dir == '':
            output_dir = os.path.join(self.data_path, 'h5')
        if len(scenes) == 0:
            scenes = self.scenes

        if not newpath(output_dir):
            print('Exit processing...')
            return

        for scene in track(scenes, description='[cyan]export h5 to %s...' % output_dir):
            pprint('processing %s...' % scene)
            fname = os.path.join(output_dir, scene + '.h5')
            fp = h5py.File(fname, 'w')
            fp.create_dataset('coords', data=self.data[scene]['coords'], compression='gzip', dtype='float32')
            fp.create_dataset('number_returns', data=self.data[scene]['number_returns'], compression='gzip', dtype='float32')
            # fp.create_dataset('edge_flight_line', data=self.data[scene]['edge_flight_line'], compression='gzip', dtype='float32')
            fp.create_dataset('intensity', data=self.data[scene]['intensity'], compression='gzip', dtype='float32')
            fp.create_dataset('semantics', data=self.labels[scene]['semantics'], compression='gzip', dtype='int64')
            fp.create_dataset('instances', data=self.labels[scene]['instances'], compression='gzip', dtype='int64')
        print('\n[green]Exported all %d files.' % len(self.scenes))

    def load_label(self):
        pass

    def load_full_mls(self):
        pass

    def load_full_als(self):
        pass

    def vis(self, scene, type, color=None, sample_ratio=0.01):
        if type == 'pc':
            xyz = self.data[scene]['coords']
            num_points = xyz.shape[0]
            idx = np.random.choice(num_points, int(num_points * sample_ratio), replace=False)
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(xyz[idx])
            o3d.visualization.draw_geometries([pcd])

    def remote_vis(self):
        pass

    def evaluation(self):
        pass

    def sample_points(self, sample_ratio):
        attrs = self.list_attributes(False)
        attrs_v = {at.split('/')[0]: {} for at in attrs}
        for k, at_v in attrs_v.items():
            attrs_v[k] = {scene: {} for scene in self.scenes}
        for scene in track(self.scenes, description='[cyan]sampling points...'):
            xyz = self.data[scene]['coords']
            num_points = xyz.shape[0]
            idx = np.random.choice(num_points, int(num_points * sample_ratio), replace=False)
            for at in attrs:
                at1, at2 = at.split('/')
                at_v = getattr(self, at1)[scene][at2]
                assert at_v.shape[0] == num_points
                attrs_v[at1][scene][at2] = at_v[idx]
            pprint('%s is sampled: %d -> %d' %(scene, num_points, num_points*sample_ratio))

        for k, at_v in attrs_v.items():
            setattr(self, k, at_v)



    def compute_normals(self, radius=0.8):
        for scene in track(self.scenes, description='[cyan]computing normals...'):
            pprint('processing %s...' % scene)
            pcd = o3d.geometry.PointCloud()
            pcd.points = o3d.utility.Vector3dVector(self.data[scene]['coords'])

            pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(
                radius=radius, max_nn=50))
            self.data[scene]['normals'] = np.asarray(pcd.normals)


    def norm_coords(self):
        for scene in track(self.scenes, description='[cyan]translating points...'):
            xyz = self.data[scene]['coords']
            x = xyz[:, 0]
            y = xyz[:, 1]
            z = xyz[:, 2]

            xyz[:, 0] = x - x.min()
            xyz[:, 1] = y - y.min()
            xyz[:, 2] = z - z.min()
            self.data[scene]['coords'] = xyz

    def compute_statistics(self):
        pass

    def evaluator(self):
        pass

    def list_attributes(self, show=True):
        table = Table()
        table.add_column("groups", justify="center")
        table.add_column("attribute", justify="center")
        data = list(self.data[self.scenes[0]].keys()) if len(self.data) != 0 else []
        labels = list(self.labels[self.scenes[0]].keys()) if len(self.labels) != 0 else []
        gt = list(self.gt[self.scenes[0]].keys()) if len(self.gt) != 0 else []
        for row in data:
            table.add_row('data', row)
        for row in labels:
            table.add_row('label', row)
        for row in gt:
            table.add_row('gt', row)
        if show:
            print(table)
        attrs = ['data/' + at for at in data]
        attrs.extend(['labels/' + at for at in labels])
        attrs.extend(['gt/' + at for at in gt])
        return attrs

    def get_data_attribute(self, attribute, group='data'):
        attr = []
        group_data = getattr(self, group)
        if attribute not in list(group_data[self.scenes[0]].keys()):
            print('[red]This attribute does not exist, please check again using \'[yellow]whu3d.list_attribute()[/]\'')
        else:
            for scene in self.scenes:
                attr.append(group_data[scene][attribute])
        return attr

    def interprete_labels(self):
        invalid = []
        for scene in track(self.scenes, description='[cyan]interpreting labels...'):
            pprint('processing %s...' % scene)
            ins = self.labels[scene]['instances']
            sem = self.labels[scene]['semantics']
            sem_map = self.sem_map

            sem_list = list(sem_map.keys())
            NUM_CLASSES = len(sem_list)

            sem_list.extend(list(set(sem)))
            sem_extend_set = set(sem_list)
            # print(sem_extend_set - set(list(sem_map.keys())))
            try:
                assert (len(sem_extend_set) == NUM_CLASSES)
            except:
                pprint('[red][Error: label] passing %s...' % scene)
                yn = pprint('[red]Do you want to delete scene: %s (\[y]/n)?' % scene)
                if yn != 'n':
                    invalid.append(scene)
                continue

            for k in self.sem_list_no_ins:
                ins[sem == k] = k
            ins[ins == 102600] = 102400

            ins_list = list(set(ins))
            ins_map = {ins_id: i for i, ins_id in enumerate(ins_list)}


            new_sem = np.zeros(sem.shape) - 1
            new_ins = np.zeros(ins.shape) - 1
            for i in sem_map.keys():
                new_sem[sem == i] = sem_map[i]
            for i in ins_map.keys():
                new_ins[ins == i] = ins_map[i]

            self.gt[scene] = {}

            self.gt[scene]['semantics'] = new_sem
            self.gt[scene]['instances'] = new_ins

        for scene in invalid:
            self.scenes.remove(scene)
            print('%s is removed!' % scene)

    def get_download(self, full=False, src='google'):
        file = json.load('download_links.json')
        data = file[src][self.data_type][self.format] if not full else file[src]['full'][self.format]
        download_link = data['link']
        passwd = data['passwd']
        print('download link: %s \npassword: %s' %(download_link, passwd))

    def get_label_map(self):
        table = Table()
        table.add_column("label", justify="center")
        table.add_column("class", justify="center")
        table.add_column("", justify="center")
        table.add_column("gt", justify="center")
        table.add_column("class", justify="center")
        for label, gt in self.sem_map.items():
            label_cls = self.label2cat[label]
            gt_cls = self.gt2cat[gt]
            row = (str(label), label_cls, ' ', str(gt), gt_cls)
            table.add_row(*row)
        print(table)



if __name__ == '__main__':
    data_root = '/Users/hanxu/data/whu'
    scenes = ['0404', '0940']
    whu3d = WHU3D(data_root=data_root, data_type='mls', format='h5', scenes=scenes)
    # whu3d.vis('0404', 'pc')
    # whu3d.export_h5()
    whu3d.get_label_map()
    attr = whu3d.get_data_attribute('coords')
    whu3d.list_attributes()
    whu3d.interprete_labels()
    whu3d.list_attributes()
    whu3d.sample_points(0.1)
    whu3d.sample_points(0.1)