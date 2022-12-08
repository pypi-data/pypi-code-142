import openfdem as fd
import matplotlib
import matplotlib.pyplot as plt

'''
Default MATPLOTLIB Fonts
'''

# plt.rcParams['figure.constrained_layout.use'] = True
plt.rcParams["figure.figsize"] = [5, 5]
matplotlib.rcParams['font.family'] = ['arial']
matplotlib.rcParams['font.size'] = 8

print("Loading Model")
# To load the model, use the directory location
model = fd.Model(r'/external/HC_160000', 'vtp')

temp_info_for_cell_1683 = model.extract_cell_info(cell_id=1683, arrays_needed=['temperature'], progress_bar=True)
print(temp_info_for_cell_1683)

for i in range(0,2):
    cell_no = model.find_cell([i, i, 0])
    print("At location %s-%s, the nearest cell ID is %s" % (i, i, cell_no) )
    cell_info = model.extract_cell_info(cell_id=cell_no, arrays_needed=['temperature'], progress_bar=True)
    plt.plot(cell_info['temperature_N1'], label=cell_no)
plt.ylim(450, 500)
plt.legend()
plt.show()