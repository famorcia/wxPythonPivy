# wxPythonPivy Porting on wxWidgets of Coin3D (a.k.a Open Inventor) examples
# Copyright (C) 2022  Fabrizio Morciano

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

import wx.glcanvas
from TestGLCanvas import TestGLCanvas


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        try:
            wx.Frame.__init__(self,
                              parent,
                              id=wx.ID_ANY,
                              title=title,  # wx.EmptyString,
                              pos=wx.DefaultPosition,
                              size=wx.Size(500, 300),
                              style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
            self.Show(True)
            attribs = [wx.glcanvas.WX_GL_DEPTH_SIZE, 32]
            TestGLCanvas(self, attribs)

        except Exception as e:
            print(e)

    def __del__(self):
        pass
