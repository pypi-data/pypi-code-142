from numba import njit
import numpy as np
import matplotlib.pyplot as plt

class Field():
    '''
    !!NEEDS NUMPY AND NUMBA TO FUNCTION!!\n
    Class for calculating and plotting electromagnetic fields and potentials in 3d. Requires numba and numpy\n\n
    
    efield, epot - Field and potential from point charge\n
    efieldLine, epotLine - Field and potential from line charge parallel to x, y or z axis. Can be placed anywhere in 3D\n
    
    efieldCircle, epotCirle - Field and potential from circle charge in origin\n
    Bfield_line - Field from line current parallel to x, y or z axis. Can be placed anywhere in 3D\n
    BfieldCircle - Field from circular current in origin\n\n
    
    PlotVector - Plots vector field. Customize colorscheme, density, and figsize\n
    PlotContour - Plots vector field. Customize colorscheme, levels, norm and figsize\
    '''
    
    @staticmethod
    @njit
    def Efield(r, particle_pos, q, eps = 8.854187817E-12):
        '''
        Calculates electric field from point charge
        r - [x,y,z] point of observation\n
        particle_pos - [x,y,z] particle position\n
        q - Charge of particle\n
        ϵ - permittivity
        '''
        ϵ = eps
        
        R = r - particle_pos
        R_norm = np.linalg.norm(R)
        E = q/(4*np.pi*ϵ) * (R/R_norm**3)
        
        return E

    @staticmethod
    @njit
    def Epot(r, particle_pos, q, eps = 8.854187817E-12):
        '''
        Calculates electric potential from point charge
        r - [x,y,z] point of observation\n
        particle_pos - [x,y,z] particle position\n
        q - Charge of particle\n
        ϵ - permittivity
        '''
        ϵ = eps
        
        R_norm = np.linalg.norm(r-particle_pos)
        V = q/(4*np.pi*ϵ*R_norm)
        return V

    @staticmethod
    @njit
    def EfieldLine(r, q, line_length, axis, x = 0, y = 0, z = 0, eps = 8.854187817E-12, N = 100):
        '''
        Calculates electric field from line charge parallel with either x, y or z axis\n
        r - [x,y,z] point of observation\n
        q - Charge of particle\n
        line_length - Length of charged line\n
        axis - ("x", "y", "z") Axis which line charge is parallel\n
        x - x coordinate of line center\n
        y - y coordinate of line center\n
        z - z coordinate of line center\n
        N - Accuracy, the higher the better, but slower. Default is 100
        ϵ - permittivity, default is vacuum
        '''
        ϵ = eps
        
        E = np.zeros(3)
        dl = line_length/N
        dq = q/N
        
        if axis == 'x':
            for i in range(N):
                r_q = np.array([-line_length/2 + i*dl +x , y, z])
                R = r - r_q
                R_norm = np.linalg.norm(R) 
                E += dq/(4*np.pi*ϵ) * R/R_norm**3
                
            return E
        
        elif axis == 'y':
            for i in range(N):
                r_q = np.array([x, -line_length/2 + i*dl + y, z])
                R = r - r_q
                R_norm = np.linalg.norm(R) 
                E += dq/(4*np.pi*ϵ) * R/R_norm**3
                
            return E            
        
        elif axis == 'z':
            for i in range(N):
                r_q = np.array([x, y, -line_length/2 + i*dl + z])
                R = r - r_q
                R_norm = np.linalg.norm(R) 
                E += dq/(4*np.pi*ϵ) * R/R_norm**3
                
            return E  
        
        else:
            raise ValueError("Argument axis must be either 'x', 'y', or 'z'")


    @staticmethod
    @njit
    def EpotLine(r, q, line_length, axis, x = 0, y = 0, z = 0, eps = 8.854187817E-12, N = 100):
        '''
        Calculates electric potential from line charge parallel with either x, y or z axis 
        r - [x,y,z] point of observation\n
        q - Charge of particle\n
        line_length - Length of charged line\n
        axis - ("x", "y", "z") Axis which line charge is parallel\n
        x - x coordinate of line center\n
        y - y coordinate of line center\n
        z - z coordinate of line center\n
        N - Accuracy, the higher the better, but slower. Default is 100
        ϵ - permittivity, default is vacuum
        '''
        ϵ = eps
        
        V = 0
        dl = line_length/N
        dq = q/N
        
        if axis == 'x':
            for i in range(N):
                r_q = np.array([-line_length/2 + i*dl +x , y, z])
                R = r - r_q
                R_norm = np.linalg.norm(R) 
                V += dq/(4*np.pi*ϵ*R_norm)
                
            return V
        
        elif axis == 'y':
            for i in range(N):
                r_q = np.array([x, -line_length/2 + i*dl + y, z])
                R = r - r_q
                R_norm = np.linalg.norm(R) 
                V += dq/(4*np.pi*ϵ*R_norm)
                
            return V            
        
        elif axis == 'z':
            for i in range(N):
                r_q = np.array([x, y, -line_length/2 + i*dl + z])
                R = r - r_q
                R_norm = np.linalg.norm(R) 
                V += dq/(4*np.pi*ϵ*R_norm)
                
            return V  
        
        else:
            raise ValueError("Argument axis must be either 'x', 'y', or 'z'")
        

    @staticmethod
    @njit
    def EfieldCircle(r, q, rad, plane, eps = 8.854187817E-12, N = 100):
        '''
        Calculates electric field from circular charge centered in origin 
        r - [x,y,z] point of observation\n
        q - Charge of circle\n
        rad - radius of cicle
        N - Accuracy, the higher the better, but slower. Default is 100
        ϵ - permittivity, default is vacuum
        '''
        ϵ = eps
        
        E = np.zeros(3)
        
        if np.linalg.norm(r) < rad:
            return np.array([0.0, 0.0, 0.0])
        
        else:
            dq = q/N
            
            if plane == 'xy':
                for i in range(N):
                    θ = 2*np.pi/N * i
                    r_q = rad * np.array([np.cos(θ), np.sin(θ), 0.0])
                    R = r - r_q
                    R_norm = np.linalg.norm(R)
                    E += dq/(4*np.pi*ϵ) * R/R_norm**3
                    
                return E

            elif plane == 'xz':
                for i in range(N):
                    θ = 2*np.pi/N * i
                    r_q = rad * np.array([np.cos(θ), 0.0, np.sin(θ)])
                    R = r - r_q
                    R_norm = np.linalg.norm(R)
                    E += dq/(4*np.pi*ϵ) * R/R_norm**3
                    
                return E
            
            elif plane == 'yz':
                for i in range(N):
                    θ = 2*np.pi/N * i
                    r_q = rad * np.array([0.0, np.cos(θ), np.sin(θ)])
                    R = r - r_q
                    R_norm = np.linalg.norm(R)
                    E += dq/(4*np.pi*ϵ) * R/R_norm**3
                    
                return E

            else:
                raise ValueError("Argument 'plane' must be either 'xy', 'xz', or 'yz'")


        
    @staticmethod
    @njit
    def EpotCirle(r, q, rad, plane, eps = 8.854187817E-12, N = 100):
        '''
        Calculates electric potential from circular charge centered in origin 
        r - [x,y,z] point of observation\n
        q - Charge of circle\n
        rad - radius of cicle
        N - Accuracy, the higher the better, but slower. Default is 100
        ϵ - permittivity, default is vacuum
        '''
        ϵ = eps
        
        V = 0
        dq = q/N
    
        if plane == 'xy':
            if np.linalg.norm(r) < rad and r[2] == 0:
                return q/(4*np.pi*ϵ*rad)
            
            else:
                for i in range(N):
                    θ = 2*np.pi/N * i
                    r_q = rad * np.array([np.cos(θ), np.sin(θ), 0.0])
                    R = r - r_q
                    R_norm = np.linalg.norm(R)
                    V += dq/(4*np.pi*ϵ*R_norm)
                
                return V

        elif plane == 'xz':
            if np.linalg.norm(r) < rad and r[1] == 0:
                return q/(4*np.pi*ϵ*rad)
            
            else:
                for i in range(N):
                    θ = 2*np.pi/N * i
                    r_q = rad * np.array([np.cos(θ), 0.0, np.sin(θ)])
                    R = r - r_q
                    R_norm = np.linalg.norm(R)
                    V += dq/(4*np.pi*ϵ*R_norm)
                
                return V
        
        elif plane == 'yz':
            if np.linalg.norm(r) < rad and r[0] == 0:
                return q/(4*np.pi*ϵ*rad)
            
            else:
                for i in range(N):
                    θ = 2*np.pi/N * i
                    r_q = rad * np.array([0.0, np.cos(θ), np.sin(θ)])
                    R = r - r_q
                    R_norm = np.linalg.norm(R)
                    V += dq/(4*np.pi*ϵ*R_norm)
                    
                return V
        else:
            raise ValueError("Argument 'plane' must be either 'xy', 'xz', or 'yz'")
    
    @staticmethod
    @njit
    def BfieldLine(r, line_length, I, axis, x = 0, y = 0, z = 0, mu = 4*np.pi*1E-7, N = 100):
        '''
        Calculates magnetic field from line current parallel to x, y or z axis. Can be placed anywhere in 3D\n
        r - [x,y,z] point of observation\n
        line_length - Length of the line\n
        I - Magnitude of current\n
        axis - ('x', 'y', 'z') which axis line runs parallel\n
        x, y, z - How much to shift the line in x, y or z direction\n
        μ - Permeability of magnetic field, vacuum being default\n
        N - Accuracy, the higher the better, but slower. Default is 100
        '''
        μ = mu
        B = np.zeros(3)
        line_segment = line_length/N
        
        if axis == 'x':
            dl = line_segment * np.array([1.0, 0.0 , 0.0 ])
            for i in range(N):
                di = np.array([-line_length/2 + line_segment*i + x, 0.0 + y, 0.0 + z])
                R = r - di
                R_norm = np.linalg.norm(R)
                B += μ/(4*np.pi)* I/R_norm**3 * np.cross(dl, R)
            
            return B
        
        elif axis == 'y':
            dl = line_segment * np.array([0.0, 1.0 , 0.0 ])
            for i in range(N):
                di = np.array([0.0 +x, -line_length/2 + line_segment*i + y, 0.0 + z])
                R = r - di
                R_norm = np.linalg.norm(R)
                B += μ/(4*np.pi)* I/R_norm**3 * np.cross(dl, R)
            
            return B
    
        elif axis == 'z':
            dl = line_segment * np.array([0.0, 0.0 , 1.0 ])
            for i in range(N):
                di = np.array([0.0 + x, 0.0 + y, -line_length/2 + line_segment*i + z])
                R = r - di
                R_norm = np.linalg.norm(R)
                B += μ/(4*np.pi)* I/R_norm**3 * np.cross(dl, R)
            
            return B

        else:
            raise ValueError("Argument axis must be either 'x', 'y', or 'z'")
    
    @staticmethod
    @njit
    def BfieldCircle(r, rad, I, mu = 4*np.pi*1E-7, N = 100):
        '''
        Calculates magnetic field from circular current parallel to x, y or z axis. Can be placed anywhere in 3D\n
        r - [x,y,z] point of observation\n
        rad - Radius of the circle\n
        I - Magnitude of current\n
        μ - Permeability of magnetic field, vacuum being default\n
        N - Accuracy, the higher the better, but slower. Default is 100
        '''
        μ = mu
        
        dθ = 2*np.pi/N 
        dl = rad*2*np.pi/N
        B = np.zeros(3)
        for i in range(N):
            current_pos = rad*np.array([np.cos(dθ*i), np.sin(dθ*i), 0])
            Idl         = I*dl*np.array([-np.sin(dθ*i), np.cos(dθ*i), 0])
            R           = r - current_pos
            R_norm      = np.linalg.norm(R)
            B          += μ/(4*np.pi)* np.cross(Idl, R)/R_norm**3
        return B
        
    @staticmethod
    def PlotVector(x1, x2, u, v, type, title = '', figsize=(16,9), broken_streamlines = False, density = 1, cmap = 'cool', equal = False, show = False, log10 = True):
        '''
        Function which plots vector\n
        x1, x2 - Arrays containing the meshgrid\n
        u, v - Arrays containing the values of the vectors at each point in the grid\n
        type - ('stream', 'quiver') Choose whether to do a streamplot or quiver\n
        title - title of the plot\n
        figsize - (M, N) size of the plot, default is (16,9)\n
        broken_streamlines = Default is False\n
        density - How dense the plot will be filled, default is 1\n
        cmap - Color map to use, default is 'cool'\n
        equal - Wether to set axis equal, default is False \n
        show - Whether to show the figure, default is False\n
        log10 - If to use log10 of colors. Makes for a smoother transition, default is True
        '''
        mag = np.sqrt(u**2 + v**2)
        U = u/mag
        V = v/mag
        if log10:
            color = np.log10(mag)
        else:
            color = mag
            
            
        plt.figure(figsize=figsize)
        
        if type == 'stream':
            plt.streamplot(x1, x2, U, V, broken_streamlines = broken_streamlines, density = density, color = color, cmap = cmap)
            plt.title(title)
            plt.colorbar()
            
        elif type == 'quiver':
            plt.quiver(x1, x2, U, V, color, cmap = cmap)
            plt.title(title)
            plt.colorbar() 
            
        else:
            raise ValueError('"type" must be either "stream" or "quiver"')       
        
        if equal:
            plt.axis('equal')
            
        if show:
            plt.show()

        
    @staticmethod
    def PlotContour(x1, x2, V, title = '', figsize = (16,9), levels = 100, norm = 'log', cmap = 'inferno', equal = False, show = False):
        '''
        Function which plots potential\n
        x1, x2 - Arrays containing the meshgrid\n
        V - Array containing the values of the potential at each point in the grid\n
        title - title of the plot\n
        figsize - (M, N) size of the plot, default is (16,9)\n
        levels - How many the contour plot will show, default is 100
        density - How dense the plot will be filled, default is 1\n
        cmap - Color map to use, default is 'cool'\n
        equal - Wether to set axis equal, default is False \n
        show - Whether to show the figure, default is False\n
        '''
        
        plt.figure(figsize = figsize)
        if equal:
            plt.axis('equal')
        plt.contour(x1, x2, V, levels = levels, norm = norm, cmap = cmap)
        plt.contourf(x1, x2, V, levels = levels, norm = norm, cmap = cmap)
        plt.title(title)
        plt.colorbar()
        
        if show:
            plt.show()