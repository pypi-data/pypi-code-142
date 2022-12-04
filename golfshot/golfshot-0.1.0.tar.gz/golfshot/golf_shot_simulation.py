import math
import numpy as np
#TODO:
# warnings about bounds on velocity, angle, rotation rate

class GolfShot:
    def __init__(self, launch_velocity=75, launch_angle=16, rotation_rate=300, g_mag=9.81):
        """Initialize golf shot simulation parameters
        
        :param launch_velocity:
            Launch velocity magnitude of the golf ball (meters per second)
        
        :param launch_angle:
            Launch angle of the ball off the club face from the horizon (degrees)
        
        :param rotation_rate:
            Backspin on the golf ball as it leaves the club face (radians per second)
        """
        self.launch_velocity = launch_velocity # m/s
        self.launch_angle = launch_angle # launch angle in degrees
        self.rotation_rate = rotation_rate # rad/s
        self._r = 0.0215 # radius of golf ball (m)
        self.g = -abs(g_mag) # (m/s/s)
        self._m = 0.0459 # golf ball mass (kg)
        self._A = math.pi*self._r**2 

    def run_sim(self):
        """Run golf shot numerical simulation and return results.

        :return:
            [list of x coordinate positions (yards), list of y coordinate positions (yards)]
        """
        # map object variables to those in the function for cleaner code
        initial_velocity = self.launch_velocity
        launch_angle = self.launch_angle
        rotation_rate = self.rotation_rate
        g = self.g
        r = self._r
        m = self._m
        D = self._r*2 # golf ball diameter
        A = self._A 

        kin_visc = 1.48*10**-5 # kinematic viscosity of air at 15*C ( m^2/s )
        rho = 1.225 # density of air at sea level, 15*C, no humidity ( kg/(m^3) )
        
        alpha0 = math.radians(launch_angle)
        v0_norm = initial_velocity
        meters_to_yards_coeff = 1.09361

        # initialize state - position, velocity, and acceleration
        # simulation is 2D. Thus, all z componenents are zero

        # initial position is our origin - all zeros
        pos0 = [0, 0, 0]

        # initial velocity vector is a function of our launch angle and launch velocity magnitude
        vel0 = [v0_norm*math.cos(alpha0),
                v0_norm*math.sin(alpha0),
                0]

        # only initial acceleration is gravity
        accel0 = [0, g, 0]

        # combine acceleration, velocity, and position into state array
        state = np.array([[pos0, vel0, accel0]])

        # parameters for executing the simulation
        sim_time = 100 # 100s should be more than plenty of time
        steps = 10000 # number of steps in the simulation
        delta_t = sim_time/steps # change in time between each sim step
        time = np.linspace(0, sim_time, num=steps) # time vector for sim

        # start the numerical simulation
        for curr_time in time:
            # compute magnitude of our velocity vector
            V = np.linalg.norm(state[-1,1,:])

            # get reynolds number for the current ball velocity
            Re = V*D/kin_visc

            # Compute drag coefficient based on reynolds numbers. Diff equations for high and low speeds
            if V <= 32:
                c_D = 1.29*10**-10*Re**2 - 2.59*10**-5*Re + 1.50   
            else:
                c_D = 1.91*10**-11*Re**2 - 5.40*10**-6*Re + 0.56 

            # compute acceleration due to drag on the golf ball
            a_D = V**2*c_D*rho*A/(2*m)
            
            # compute non-dimensional spin factor S
            S = rotation_rate*r/V

            # compute the lift coefficient. Function of spin factor
            c_L = -3.25*S**2 + 1.99*S

            # compute acceleration due to lift
            a_L = V**2*c_L*rho*A/2/m 

            # compute current ball path angle from velocity vector
            angle = math.atan(state[-1,1,1]/state[-1,1,0]) 

            # compute acceleration in each axis
            # drag acceleration acts opposite the ball path
            # lift acceleration acts orthogonal to ball path
            a_x = -a_D*math.cos(angle) - a_L*math.sin(angle)
            a_y = -a_D*math.sin(angle) + a_L*math.cos(angle) + g
            a_z = 0

            # compute velocity in each axis
            v_x = state[-1,1,0] + a_x*delta_t
            v_y = state[-1,1,1] + a_y*delta_t
            v_z = 0

            # compute position
            x = state[-1,0,0] + v_x*delta_t
            y = state[-1,0,1] + v_y*delta_t
            z = 0
            
            # consolidate state array and append to previous states
            state = np.append(state,[[[x, y, z], [v_x, v_y, v_z], [a_x, a_y, a_z]]],0)

            # if the height of the ball drops below 0 on the y axis, we know the ball has hit the ground
            if y < 0:
                break
        
        # pull out x and y states for 2D sim
        pos_x = (state[:,0,0]*meters_to_yards_coeff).tolist()
        pos_y = (state[:,0,1]*meters_to_yards_coeff).tolist()

        return [pos_x, pos_y] # return 2D state