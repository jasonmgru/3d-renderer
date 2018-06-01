import numpy as np

class Wireframe:
    def __init__(self, node_list, face_list):
        self._faces = face_list

        ones_col = np.ones((len(node_list), 1))
        self._nodes = np.array(node_list)
        self._nodes = np.hstack((self._nodes, ones_col))

        self._selected = False

    def nodes(self):
        return self._nodes

    def faces(self):
        return self._faces

    def transform(self, matrix):
        self._nodes = np.dot(self._nodes, matrix)

    def translate(self, dx, dy, dz):
        matrix = [[1, 0, 0, 0], \
                  [0, 1, 0, 0], \
                  [0, 0, 1, 0], \
                  [dx, dy, dz, 1]]

        self.transform(matrix)

    def scale(self, sx, sy, sz):
        matrix = [[sx, 0, 0, 0], \
                  [0, sy, 0, 0], \
                  [0, 0, sz, 0], \
                  [0, 0, 0, 1]]
        
        cen = self.center()
        self.translate(-cen[0], -cen[1], -cen[2])
        self.transform(matrix)
        self.translate(cen[0], cen[1], cen[2])

    def rotate_x(self, angle):
        c = np.cos(angle)
        s = np.sin(angle)
        matrix = [[1, 0, 0, 0] , \
                  [0, c, -s, 0], \
                  [0, s, c, 0], \
                  [0, 0, 0, 1]]

        cen = self.center()
        self.translate(-cen[0], -cen[1], -cen[2])
        self.transform(matrix)
        self.translate(cen[0], cen[1], cen[2])

    def rotate_y(self, angle):
        c = np.cos(angle)
        s = np.sin(angle)

        matrix = [[c, 0, -s, 0], \
                  [0, 1, 0, 0], \
                  [s, 0, c, 0], \
                  [0, 0, 0, 1]]

        cen = self.center()
        self.translate(-cen[0], -cen[1], -cen[2])
        self.transform(matrix)
        self.translate(cen[0], cen[1], cen[2])

    def rotate_z(self, angle):
        c = np.cos(angle)
        s = np.sin(angle)

        matrix = [[c, -s, 0, 0], \
                  [s, c, 0, 0], \
                  [0, 0, 1, 0], \
                  [0, 0, 0, 1]]

        cen = self.center()
        self.translate(-cen[0], -cen[1], -cen[2])
        self.transform(matrix)
        self.translate(cen[0], cen[1], cen[2])

    def center(self):
        num_nodes = len(self._nodes)
        mean_x = sum([n[0] for n in self._nodes]) / num_nodes
        mean_y = sum([n[1] for n in self._nodes]) / num_nodes
        mean_z = sum([n[2] for n in self._nodes]) / num_nodes

        return (mean_x, mean_y, mean_z)

    def perp(self, face):
        face_points = self.get_points(face)

        a = np.subtract(face_points[2], face_points[0])
        b = np.subtract(face_points[2], face_points[1])

        return np.cross(a, b)

    def get_points(self, face, dim=3):
        face_points = []
        i = 0
        for n in face:
            if i == 3:
                break
            i += 1
            face_points.append(self._nodes[n][:dim])

        return face_points

    def set_selected(self, selected_bool):
        self._selected = selected_bool

    def selected(self):
        return self._selected