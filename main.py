data = 'area.txt'

import pandas as pd
import open3d as o3d

print('\n----- Import Done -----')

print('\nReading Data...')

'''
with open(data, 'r') as file:
    for line in file:
      print(line)
'''

point_cloud_data = pd.read_csv(data, sep=' ', header=None, names=['X', 'Y', 'Z', 'Column4', 'Column5', 'Column6']) #adjust the names accordingly

print(point_cloud_data.head())

print(point_cloud_data.shape)

print('\n----- Point_Array step begins! -----')

x_median = point_cloud_data['X'].median()
y_median = point_cloud_data['Y'].median()

# Split based on X and Y medians

part1 = point_cloud_data[(point_cloud_data['X'] <= x_median) & (point_cloud_data['Y'] <= y_median)]
part2 = point_cloud_data[(point_cloud_data['X'] > x_median) & (point_cloud_data['Y'] <= y_median)]
part3 = point_cloud_data[(point_cloud_data['X'] <= x_median) & (point_cloud_data['Y'] > y_median)]
part4 = point_cloud_data[(point_cloud_data['X'] > x_median) & (point_cloud_data['Y'] > y_median)]

#The following function converts DataFrame to Open3D PointCloud object

def dataframe_to_pointcloud(df):
    points = df[['X', 'Y', 'Z']].to_numpy()
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    return pcd

# Convert each part to Open3D PointCloud objects
part1_pcd = dataframe_to_pointcloud(part1)  #Figure-2 Section-1
part2_pcd = dataframe_to_pointcloud(part2)  #Figure-3 Section-2
part3_pcd = dataframe_to_pointcloud(part3)  #Figure-4 Section-3
part4_pcd = dataframe_to_pointcloud(part4)  #Figure-5 Section-4

# Visualize the parts one-by-one
#o3d.visualization.draw_geometries([part1_pcd, part2_pcd, part3_pcd, part4_pcd])    #Display Figure-1, whole point cloud of a street view
o3d.visualization.draw_geometries([part1_pcd])  #Display Figure-2 Section-1
o3d.visualization.draw_geometries([part2_pcd])  #Display Figure-3 Section-2
o3d.visualization.draw_geometries([part3_pcd])  #Display Figure-4 Section-3
o3d.visualization.draw_geometries([part4_pcd])  #Display Figure-5 Section-4