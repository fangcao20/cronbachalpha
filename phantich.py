import pandas as pd
import psython as psy
import re
import random


def phantichfile(filename):
  df = pd.read_excel(filename)
  data = psy.cronbach_alpha_scale_if_deleted(df)
  return data


# Tính tần số
def CountFrequency(my_list):
  freq = {}
  for item in my_list:
    if item in freq:
      freq[item] += 1
    else:
      freq[item] = 1
  return freq


# Gộp nhóm các biến
def nhom_label(my_dict):
  group_key = []
  for key in my_dict.keys():
    found = False
    for sublist in group_key:
      if sublist and re.split(r'(\d+)', key)[0] == re.split(
          r'(\d+)', sublist[0])[0]:
        sublist.append(key)
        found = True
        break
    if not found:
      group_key.append([key])
  return group_key


# Tính tần số của các kết quả
def nhom_value(my_dict):
  data_list = [(k, v) for k, v in my_dict.items()]
  new_dict = {}
  for item in data_list:
    new_value = CountFrequency(item[1].values())
    for i in range(0, 5):
      if i not in new_value.keys():
        new_value[i] = 0
    sorted_value = {k: new_value[k] for k in sorted(new_value)}
    new_dict[item[0]] = sorted_value
  return new_dict


def ve_bieu_do(filename):
  df = pd.read_excel(filename)
  data = df.to_dict()
  group_labels = nhom_label(data)
  group_datas = nhom_value(data)
  list_datasets = []
  #Tạo datasets
  for g_label in group_labels:
    datasets = []
    for label in g_label:
      r = random.randrange(255)
      g = random.randrange(255)
      b = random.randrange(255)
      list_color = []
      for i in range(0, 5):
        list_color.append(f'rgba({r}, {g}, {b}, 0.2')
      dataset = {
        'label': label,
        'data': list(group_datas[label].values()),
        'backgroundColor': list_color
      }
      datasets.append(dataset)
    list_datasets.append(datasets)
  return list_datasets


# df = pd.read_excel('Demo-file.xlsx')
# data = df.to_dict()
# group_labels = nhom_label(data)
# group_datas = nhom_value(data)
# print(group_labels)
# print(group_datas)

# #Tạo datasets
# for g_label in group_labels:
#     datasets = []
#     r = 255
#     g = 99
#     b = 132
#     for label in g_label:
#         list_color = []
#         for i in range(0, 5):
#             list_color.append(f'rgba({r}, {g}, {b}, 0.2')
#         dataset = {'label': label, 'data': group_datas[label].values(), 'backgroundColor': list_color}
#         datasets.append(dataset)
#         g += 2
#         b += 2

#     print(datasets)
