import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve, LinearOperator, gmres
from scipy.linalg import norm
from scipy.sparse import diags
import matplotlib.pyplot as plt
import types


# generic class only implement algo. didn't implement detail func about M0, UT, etc.
class MfgBase(object):
    # it's a base class which implements the policy iteration
    def __init__(
        self, Q_guess=None, nv=0.05, x1=0, x2=1, Nx=200, Nt=200, T=1.0, bc="periodic"
    ):
        self.Nt = Nt
        self.bc = bc
        if bc == "periodic":
            self.xs = np.linspace(x1, x2, Nx + 1)[:-1]  # grid on space
        elif bc == "dirichlet":
            self.xs = np.linspace(x1, x2, Nx + 1)[1:-1]  # grid on space
        elif bc == "neumann":
            self.xs = np.linspace(x1, x2, Nx + 1)  # grid on space
        self.Nx = self.xs.shape[0]
        self.dx = self.xs[1] - self.xs[0]
        self.ts = np.linspace(0, T, Nt + 1)  # grid on time
        self.T = self.ts[-1]
        self.dt = self.ts[1] - self.ts[0]
        self.nv = nv  # diffusion paramter
        # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)

        # initail condition and terminal condition
        M0 = self.M0_func(self.xs)
        self.M0 = M0 / np.sum(M0) / self.dx
        try:
            self.UT = self.UT_func(self.xs)
        except NotImplementedError:
            # no use self.UT
            pass

        # array to store solution
        self.U = np.zeros((self.Nt, self.Nx))  # t = 0 ... (T-dt)
        self.M = np.ones((self.Nt, self.Nx))  # t = dt ... T
        self.M_bar = np.copy(self.M)  # using in fp
        self.M_old = np.copy(self.M)
        self.U_old = np.copy(self.U)

        # initial guess about Q
        if isinstance(Q_guess, types.FunctionType):
            q0 = Q_guess(self.xs)
            q0 = np.tile(q0, (self.Nt, 1))
            self.QL = np.maximum(q0, 0)
            self.QR = np.minimum(q0, 0)
        elif isinstance(Q_guess, np.ndarray):
            self.QL = np.copy(Q_guess[0])
            self.QR = np.copy(Q_guess[1])
        else:
            self.QL = np.zeros((self.Nt, self.Nx))
            self.QR = np.zeros((self.Nt, self.Nx))
        self.QL_old = np.copy(self.QL)
        self.QR_old = np.copy(self.QR)

        # some lists to log residual or something else
        self.residual_FP_history = []  # list to store history of residual
        self.residual_HJB_history = []  # list to store history of residual
        self.sol_M_history = []  # list to store history of L-inf disatance
        self.sol_U_history = []  # list to store history of L-2 disatance
        self.Laplace = self.build_Laplace(bc)
        self.DL, self.DR = self.build_D(bc)
        self.A_fixp = sparse.eye(self.Nx) - self.dt * self.Laplace
        return

    def build_Laplace(self, bc="periodic"):
        if bc == "periodic":
            dim_one_laplace = diags(
                [1, 1, -2, 1, 1],
                [1 - self.Nx, -1, 0, 1, self.Nx - 1],
                shape=(self.Nx, self.Nx),
                format="csr",
            )
            dim_one_laplace = self.nv / self.dx**2 * dim_one_laplace
            return dim_one_laplace
        elif bc == "dirichlet":
            dim_one_laplace = diags(
                [1, -2, 1], [-1, 0, 1], shape=(self.Nx, self.Nx), format="csr"
            )
            dim_one_laplace = self.nv / self.dx**2 * dim_one_laplace
            return dim_one_laplace
        elif bc == "neumann":
            dim_one_laplace = diags(
                [1, -2, 1], [-1, 0, 1], shape=(self.Nx, self.Nx), format="csr"
            )
            dim_one_laplace[0, 0] += 1
            dim_one_laplace[-1, -1] += 1
            dim_one_laplace = self.nv / self.dx**2 * dim_one_laplace
            return dim_one_laplace
        else:
            raise NotImplementedError("unsupported boundary condition")

    def build_D(self, bc="periodic"):
        if bc == "periodic":
            DL = (
                diags(
                    [-1, 1, -1],
                    [-1, 0, self.Nx - 1],
                    shape=(self.Nx, self.Nx),
                    format="csr",
                )
                / self.dx
            )
            DR = (
                diags(
                    [1, -1, 1],
                    [1 - self.Nx, 0, 1],
                    shape=(self.Nx, self.Nx),
                    format="csr",
                )
                / self.dx
            )
            return DL, DR
        elif bc == "dirichlet":
            DL = (
                diags(
                    [-1, 1],
                    [-1, 0],
                    shape=(self.Nx, self.Nx),
                    format="csr",
                )
                / self.dx
            )
            DR = (
                diags([-1, 1], [0, 1], shape=(self.Nx, self.Nx), format="csr") / self.dx
            )
            return DL, DR
        elif bc == "neumann":
            DL = (
                diags([-1, 1], [-1, 0], shape=(self.Nx, self.Nx), format="csr")
                / self.dx
            )
            DR = (
                diags([-1, 1], [0, 1], shape=(self.Nx, self.Nx), format="csr") / self.dx
            )
            self.DL_div = DL.copy()
            self.DR_div = DR.copy()
            DL[0, 0] = 0.0
            DR[-1, -1] = 0.0
            return DL, DR
        else:
            raise NotImplementedError("unsupported boundary condition")

    # initial condition
    def M0_func(self, x):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    # final condition
    def UT_func(self, x):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement UT_func")

    def get_UT(self, mT):
        # a defualt function to get UT
        # if you want to use a different UT, you can rewrite this function
        # especially, if UT is a function of x and M at end time
        # like UT = np.sum(self.xs*mT)*self.dx*self.xs
        return self.UT

    # default hamilton
    # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)
    def F1_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement F1_func")

    def F2_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement F2_func")

    def optimal_control(self, m, du):
        return du / self.F1_func(m)

    def running_cost(self, m, q):
        ql, qr = q  # unpack
        q2 = ql**2 + qr**2
        return 0.5 * self.F1_func(m) * q2 + self.F2_func(m)

    def hjb_rhs(self, u, q, m):
        """
        rhs of HJB equation
        """
        return u + self.dt * self.running_cost(m, q)

    def hjb_rhs_fixp(self, u, du2, m):
        """
        rhs of HJB equation
        """
        rhs = u - self.dt * (0.5 * du2 / self.F1_func(m) - self.F2_func(m))
        return rhs

    def logging_solution(self, M, U):
        self.sol_M_history.append(np.copy(M))
        self.sol_U_history.append(np.copy(U))
        return

    def linearOP_FP(self, q):
        ql, qr = q  # unpack
        tmp1 = sparse.eye(self.Nx)
        tmp2 = self.Laplace
        if self.bc == "neumann":
            tmp3 = self.DL_div @ sparse.diags(qr) + self.DR_div @ sparse.diags(ql)
        else:
            tmp3 = self.DL @ sparse.diags(qr) + self.DR @ sparse.diags(ql)
        return tmp1 - self.dt * (tmp2 + tmp3)

    def solve_FP(self, Q):
        """
        solve FP with drift Q (self.QL and self.QR)
        this method should only update self.M
        """
        QL, QR = Q  # unpack
        mn = self.M0
        for ti in range(self.Nt):
            ql = QL[ti, :]
            qr = QR[ti, :]
            q = [ql, qr]
            A = self.linearOP_FP(q)
            rhs = mn
            self.M[ti, :] = spsolve(A, rhs)
            mn = self.M[ti, :]
        return

    def linearOP_HJB(self, q):
        ql, qr = q
        tmp1 = sparse.eye(self.Nx)
        tmp2 = self.Laplace
        tmp3 = diags(ql) @ self.DL + diags(qr) @ self.DR
        return tmp1 - self.dt * (tmp2 - tmp3)

    def solve_HJB(self, M, Q):
        """
        solve linearize HJB with hamilton:
        qDu - 0.5*F1(m)*|q|^2 - F2(m)

        this method should only update self.U
        """
        QL, QR = Q  # unpack
        mT = M[-1, :]
        un = self.get_UT(mT)
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            ql = QL[ti, :]
            qr = QR[ti, :]
            q = [ql, qr]
            A = self.linearOP_HJB(q)
            rhs = self.hjb_rhs(un, q, mn)
            self.U[ti, :] = spsolve(A, rhs)
            un = self.U[ti, :]
        return

    def solve_HJB_fixp(self, M):
        """
        solve linearize HJB with hamilton:
        0.5*|Du|^2/F1(m) - F2(m)
        where Du is frezz with U_old

        this method should only update self.U
        """
        mT = M[-1, :]
        un = self.get_UT(mT)
        for ti in range(self.Nt - 1, -1, -1):
            u_old = self.U_old[ti, :]
            dul_old = np.maximum(self.DL @ u_old, 0.0)
            dur_old = np.minimum(self.DR @ u_old, 0.0)
            du2_old = dul_old**2 + dur_old**2
            mn = M[ti, :]
            lhsM = self.A_fixp
            rhs = self.hjb_rhs_fixp(un, du2_old, mn)
            self.U[ti, :] = spsolve(lhsM, rhs)
            un = self.U[ti, :]
        self.U_old = np.copy(self.U)
        return

    def update_Q(self, U, M):
        """
        this method should only update self.QL and self.QR
        """
        for ti in range(self.Nt):
            mn = M[ti, :]
            un = U[ti, :]
            dul = self.DL @ un
            dur = self.DR @ un
            self.QL[ti, :] = np.maximum(self.optimal_control(mn, dul), 0.0)
            self.QR[ti, :] = np.minimum(self.optimal_control(mn, dur), 0.0)
        # compute the diff bettwen Q and Q_old
        diff_QL = np.max(np.abs(self.QL - self.QL_old))
        diff_QR = np.max(np.abs(self.QR - self.QR_old))
        diff = np.max([diff_QL, diff_QR])
        # print(f"diff between Q = {diff}")
        self.QL_old = np.copy(self.QL)
        self.QR_old = np.copy(self.QR)
        return

    def default_fp_pn(n):
        if n == 0:
            return (0, 1)
        else:
            return (1 - 1 / (n + 1), 1 / (n + 1))

    def solve(self, maxit=10, fp=False, pn=default_fp_pn):
        # fp: bool, use fictious play or not
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(0, maxit):
            # solve FP with Q
            Q = [self.QL, self.QR]
            self.solve_FP(Q)
            # update M_bar if use fictious play
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            # update U with M_bar and Q
            self.solve_HJB(self.M_bar, Q)
            # update Q with U and M_bar
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)
            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_spi1_pn(n):
        return ((n + 1) / (n + 2), 1 / (n + 2))

    def solve_with_spi1(self, maxit=10, pn=default_spi1_pn):
        self.diff_M = []
        # init
        QL_bar = np.copy(self.QL)
        QR_bar = np.copy(self.QR)
        for i in range(0, maxit):
            # solve FP with Q_bar
            Q_bar = [QL_bar, QR_bar]
            self.solve_FP(Q_bar)
            # update U with M and Q_bar
            self.solve_HJB(self.M, Q_bar)
            # update Q with U and M
            self.update_Q(self.U, self.M)
            # update Q_bar
            p1, p2 = pn(i)
            QL_bar = p1 * QL_bar + p2 * self.QL
            QR_bar = p1 * QR_bar + p2 * self.QR
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_spi2_pn(n):
        if n == 0:
            return (0, 1)
        else:
            return (1 - 1 / (n + 1), 1 / (n + 1))

    def solve_with_spi2(self, maxit=10, pn=default_spi2_pn):
        self.diff_M = []
        # init
        QL_hat = np.copy(self.QL)
        QR_hat = np.copy(self.QR)
        self.M_bar = np.copy(self.M)
        # init W_bar, but never use this init value
        # update W_bar in first iteration with M*q
        # and average W in later iteration
        WL_bar = np.copy(self.QL)
        WR_bar = np.copy(self.QR)
        for i in range(0, maxit):
            # solve FP with Q
            Q = [self.QL, self.QR]
            self.solve_FP(Q)
            # update M_bar
            p1, p2 = pn(i)
            self.M_bar = p1 * self.M_bar + p2 * self.M
            # update Q_hat(firt compute W_bar)
            if p1 == 0:
                WL_bar = self.M * self.QL
                WR_bar = self.M * self.QR
                QL_hat = np.copy(self.QL)  # avoid error here
                QR_hat = np.copy(self.QR)
            else:
                WL_bar = p1 * WL_bar + p2 * self.M * self.QL
                WR_bar = p1 * WR_bar + p2 * self.M * self.QR
                QL_hat = WL_bar / self.M_bar  # be careful when M_bar is too small
                QR_hat = WR_bar / self.M_bar
            # update U with M and Q_hat
            Q_hat = [QL_hat, QR_hat]
            self.solve_HJB(self.M_bar, Q_hat)
            # update Q with U and M(don't consider M here)
            self.update_Q(self.U, self.M)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def solve_with_fixpoint(self, maxit=10, fp=True, pn=default_fp_pn):
        print("solving with fixed point method")
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(0, maxit):
            Q = [self.QL, self.QR]
            self.solve_FP(Q)
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            self.solve_HJB_fixp(self.M_bar)
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)

            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def compute_residual(self, M, U):
        res_fp = self.residual_FP(M, U)
        res_hjb = self.residual_HJB(M, U)
        self.residual_FP_history.append(res_fp)
        self.residual_HJB_history.append(res_hjb)
        return res_fp, res_hjb

    def residual_FP(self, M, U):
        residual_ = np.zeros_like(M)  # residual in every point
        mn = self.M0
        for ti in range(self.Nt):
            m = M[ti, :]
            un = U[ti, :]
            dul = self.DL @ un
            dur = self.DR @ un
            # q here is only a temp variable to compute residual
            ql = np.maximum(self.optimal_control(m, dul), 0.0)
            qr = np.minimum(self.optimal_control(m, dur), 0.0)
            q = [ql, qr]
            lhsM = self.linearOP_FP(q) / self.dt
            rhs = mn / self.dt
            residual_[ti, :] = lhsM @ m - rhs
            mn = M[ti, :]
        residual = np.sqrt(self.dx * self.dt) * norm(residual_)
        return residual

    def residual_HJB(self, M, U):
        residual_ = np.zeros_like(U)  # residual in every point
        mT = M[-1, :]
        un = self.get_UT(mT)
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            u = U[ti, :]
            dul = self.DL @ u
            dur = self.DR @ u
            # q here is only a temp variable to compute residual
            ql = np.maximum(self.optimal_control(mn, dul), 0.0)
            qr = np.minimum(self.optimal_control(mn, dur), 0.0)
            q = [ql, qr]
            lhsM = self.linearOP_HJB(q) / self.dt
            rhs = self.hjb_rhs(un, q, mn) / self.dt
            residual_[ti, :] = lhsM @ u - rhs
            un = U[ti, :]
        residual = np.sqrt(self.dx * self.dt) * norm(residual_)
        return residual

    def compute_cost(self):
        cost = 0.0
        mT = self.M[-1, :]
        uT = self.get_UT(mT)
        for ti in range(self.Nt):
            m = self.M[ti, :]
            u = self.U[ti, :]
            dul = self.DL @ u
            dur = self.DR @ u
            # q here is only a temp variable to compute residual
            ql = np.maximum(self.optimal_control(m, dul), 0.0)
            qr = np.minimum(self.optimal_control(m, dur), 0.0)
            q2 = ql**2 + qr**2
            cost += np.sum(
                self.dt * self.dx * m * (0.5 * self.F1_func(m) * q2 + self.F2_func(m))
            )
        cost += np.sum(self.dx * uT * self.M[-1, :])
        return cost


class MfgBase2D(object):
    # it's a base class which implements the policy iteration and fixed point iteration
    def __init__(
        self,
        Q_guess=None,
        nv=0.3,
        x1=0,
        x2=1,
        Nx=50,
        Nt=50,
        T=1.0,
        bc="periodic",
    ):
        self.Nt = Nt
        self.bc = bc
        if bc == "periodic":
            self.xs1 = np.linspace(x1, x2, Nx + 1)[:-1]  # grid on space
            self.xs2 = np.linspace(x1, x2, Nx + 1)[:-1]  # grid on space
        elif bc == "dirichlet":
            self.xs1 = np.linspace(x1, x2, Nx + 1)[1:-1]  # grid on space
            self.xs2 = np.linspace(x1, x2, Nx + 1)[1:-1]  # grid on space
        elif bc == "neumann":
            self.xs1 = np.linspace(x1, x2, Nx + 1)  # grid on space
            self.xs2 = np.linspace(x1, x2, Nx + 1)  # grid on space
        self.Nx = self.xs1.shape[0]
        self.dx = self.xs1[1] - self.xs1[0]
        self.ts = np.linspace(0, T, Nt + 1)  # grid on time
        self.dt = self.ts[1] - self.ts[0]
        self.T = self.ts[-1]
        self.nv = nv  # diffusion paramter

        # initail condition and terminal condition
        M0 = self.M0_func(self.xs1, self.xs2)
        self.M0 = M0 / np.sum(M0) / (self.dx) ** 2
        try:
            self.UT = self.UT_func(self.xs1, self.xs2)
        except NotImplementedError:
            # no use self.UT
            pass

        # array to store solution
        self.U = np.zeros((self.Nt, (self.Nx) ** 2))  # t = 0 ... (T-dt)
        self.M = np.ones((self.Nt, (self.Nx) ** 2))  # t = dt ... T
        self.M_bar = np.copy(self.M)  # using in fp
        self.M_old = np.copy(self.M)
        self.U_old = np.copy(self.U)

        # initial guess about Q
        if isinstance(Q_guess, types.FunctionType):
            xs1, xs2 = np.meshgrid(self.xs1, self.xs2)
            q0_1, q0_2 = Q_guess(xs1, xs2)
            q0_1 = q0_1.reshape(-1)
            q0_2 = q0_2.reshape(-1)
            q0_1 = np.tile(q0_1, (self.Nt, 1))
            q0_2 = np.tile(q0_2, (self.Nt, 1))
            self.QL1 = np.maximum(q0_1, 0)
            self.QR1 = np.minimum(q0_1, 0)
            self.QL2 = np.maximum(q0_2, 0)
            self.QR2 = np.minimum(q0_2, 0)
        elif isinstance(Q_guess, np.ndarray):
            self.QL1 = np.copy(Q_guess[0])
            self.QR1 = np.copy(Q_guess[1])
            self.QL2 = np.copy(Q_guess[2])
            self.QR2 = np.copy(Q_guess[3])
        else:
            self.QL1 = np.zeros((self.Nt, (self.Nx) ** 2))
            self.QR1 = np.zeros((self.Nt, (self.Nx) ** 2))
            self.QL2 = np.zeros((self.Nt, (self.Nx) ** 2))
            self.QR2 = np.zeros((self.Nt, (self.Nx) ** 2))
        self.QL1_old = np.copy(self.QL1)
        self.QR1_old = np.copy(self.QR1)
        self.QL2_old = np.copy(self.QL2)
        self.QR2_old = np.copy(self.QR2)
        self.Q = [self.QL1, self.QR1, self.QL2, self.QR2]
        self.Q_old = [self.QL1_old, self.QR1_old, self.QL2_old, self.QR2_old]

        # some lists to log residual or something else
        self.residual_FP_history = []  # list to store history of residual
        self.residual_HJB_history = []  # list to store history of residual
        self.sol_M_history = []  # list to store history of L-inf disatance
        self.sol_U_history = []  # list to store history of L-2 disatance
        self.Laplace = self.build_Laplace(bc)
        self.DL1, self.DR1, self.DL2, self.DR2 = self.build_D(bc)
        self.A_fixp = sparse.eye(self.Nx**2) - self.dt * self.Laplace
        return

    def build_Laplace(self, bc="periodic"):
        if bc == "periodic":
            dim_one_laplace = diags(
                [1, 1, -2, 1, 1], [1 - self.Nx, -1, 0, 1, self.Nx - 1], format="csr"
            )
            dim_two_laplace = sparse.kron(
                dim_one_laplace, sparse.eye(self.Nx)
            ) + sparse.kron(sparse.eye(self.Nx), dim_one_laplace)
            dim_two_laplace = self.nv / self.dx**2 * dim_two_laplace
            return dim_two_laplace
        elif bc == "dirichlet":
            dim_one_laplace = diags([1, -2, 1], [-1, 0, 1], shape=(self.Nx,self.Nx), format="csr")
            dim_two_laplace = sparse.kron(
                dim_one_laplace, sparse.eye(self.Nx)
            ) + sparse.kron(sparse.eye(self.Nx), dim_one_laplace)
            dim_two_laplace = self.nv / self.dx**2 * dim_two_laplace
            return dim_two_laplace
        elif bc == "neumann":
            dim_one_laplace = diags([1, -2, 1], [-1, 0, 1], shape=(self.Nx,self.Nx), format="csr")
            dim_one_laplace[0, 0] += 1
            dim_one_laplace[-1, -1] += 1
            dim_two_laplace = sparse.kron(
                dim_one_laplace, sparse.eye(self.Nx)
            ) + sparse.kron(sparse.eye(self.Nx), dim_one_laplace)
            dim_two_laplace = self.nv / self.dx**2 * dim_two_laplace
            return dim_two_laplace
        else:
            raise NotImplementedError("unsupported boundary condition")

    def build_D(self, bc="periodic"):
        if bc == "periodic":
            DL = diags(
                [-1, 1, -1],
                [-1, 0, self.Nx - 1],
                shape=(self.Nx, self.Nx),
                format="csr",
            )
            DR = diags(
                [1, -1, 1], [1 - self.Nx, 0, 1], shape=(self.Nx, self.Nx), format="csr"
            )
            DL1 = sparse.kron(sparse.eye(self.Nx), DL) / self.dx
            DR1 = sparse.kron(sparse.eye(self.Nx), DR) / self.dx
            DL2 = sparse.kron(DL, sparse.eye(self.Nx)) / self.dx
            DR2 = sparse.kron(DR, sparse.eye(self.Nx)) / self.dx
            return DL1, DR1, DL2, DR2
        elif bc == "dirichlet":
            DL = diags([-1, 1], [-1, 0], shape=(self.Nx, self.Nx), format="csr")
            DR = diags([-1, 1], [0, 1], shape=(self.Nx, self.Nx), format="csr")
            DL1 = sparse.kron(sparse.eye(self.Nx), DL) / self.dx
            DR1 = sparse.kron(sparse.eye(self.Nx), DR) / self.dx
            DL2 = sparse.kron(DL, sparse.eye(self.Nx)) / self.dx
            DR2 = sparse.kron(DR, sparse.eye(self.Nx)) / self.dx
            return DL1, DR1, DL2, DR2
        elif bc == "neumann":
            DL = diags([-1, 1], [-1, 0], shape=(self.Nx, self.Nx), format="csr") / self.dx
            DR = diags([-1, 1], [0, 1], shape=(self.Nx, self.Nx), format="csr") / self.dx
            DL_div = DL.copy()
            DR_div = DR.copy()
            self.DL1_div = sparse.kron(sparse.eye(self.Nx), DL_div) 
            self.DR1_div = sparse.kron(sparse.eye(self.Nx), DR_div) 
            self.DL2_div = sparse.kron(DL_div, sparse.eye(self.Nx)) 
            self.DR2_div = sparse.kron(DR_div, sparse.eye(self.Nx))
            DL[0, 0] = 0
            DR[-1, -1] = 0
            DL1 = sparse.kron(sparse.eye(self.Nx), DL) 
            DR1 = sparse.kron(sparse.eye(self.Nx), DR) 
            DL2 = sparse.kron(DL, sparse.eye(self.Nx)) 
            DR2 = sparse.kron(DR, sparse.eye(self.Nx))
            return DL1, DR1, DL2, DR2
        else:
            raise NotImplementedError("unsupported boundary condition")

    # initial condition
    # should return array with shape (self.Nx*self.Nx, )
    def M0_func(self, x1, x2):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement M0_func")

    # final condition
    # should return array with shape (self.Nx*self.Nx, )
    def UT_func(self, x1, x2):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement UT_func")

    def get_UT(self, mT):
        # a defualt function to get UT
        # if you want to use a different UT, you can rewrite this function
        # especially, if UT is a function of x and M at end time
        # like UT = np.sum(self.xs*mT)*self.dx**2*self.xs
        return self.UT

    # hamilton
    # H(Du,m) = 0.5*|Du|^2/F1(m) - F2(m)
    def F1_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement F1_func")

    def F2_func(self, m):
        raise NotImplementedError(self.__class__.__name__ + "didn't implement F2_func")

    def optimal_control(self, m, du):
        return du / self.F1_func(m)

    def running_cost(self, m, q):
        ql1, qr1, ql2, qr2 = q  # unpack
        q2 = ql1**2 + qr1**2 + ql2**2 + qr2**2
        return 0.5 * self.F1_func(m) * q2 + self.F2_func(m)

    def hjb_rhs(self, u, q, m):
        """
        rhs of HJB equation
        """
        return u + self.dt * self.running_cost(m, q)

    def hjb_rhs_fixp(self, u, du2, m):
        """
        rhs of HJB equation in fixpoint method
        """
        rhs = u - self.dt * (0.5 * du2 / self.F1_func(m) - self.F2_func(m))
        return rhs

    def logging_solution(self, M, U):
        self.sol_M_history.append(np.copy(M))
        self.sol_U_history.append(np.copy(U))
        return

    def linearOP_FP(self, q):
        ql1, qr1, ql2, qr2 = q  # unpack
        tmp1 = sparse.eye(self.Nx**2)
        tmp2 = self.Laplace
        if self.bc == "neumann":
            tmp3 = (
            self.DL1_div @ sparse.diags(qr1)
            + self.DR1_div @ sparse.diags(ql1)
            + self.DL2_div @ sparse.diags(qr2)
            + self.DR2_div @ sparse.diags(ql2)
            )
        else:
            tmp3 = (
                self.DL1 @ sparse.diags(qr1)
                + self.DR1 @ sparse.diags(ql1)
                + self.DL2 @ sparse.diags(qr2)
                + self.DR2 @ sparse.diags(ql2)
            )
        return tmp1 - self.dt * (tmp2 + tmp3)

    def solve_FP(self, Q):
        """
        solve FP with drift Q (self.QL and self.QR)
        this method should only update self.M
        """
        QL1, QR1, QL2, QR2 = Q  # unpack
        mn = self.M0
        for ti in range(self.Nt):
            ql1 = QL1[ti, :]
            qr1 = QR1[ti, :]
            ql2 = QL2[ti, :]
            qr2 = QR2[ti, :]
            q = [ql1, qr1, ql2, qr2]
            A = self.linearOP_FP(q)
            rhs = mn
            self.M[ti, :] = spsolve(A, rhs)
            mn = self.M[ti, :]
        return

    def linearOP_HJB(self, q):
        ql1, qr1, ql2, qr2 = q
        tmp1 = sparse.eye(self.Nx**2)
        tmp2 = self.Laplace
        tmp3 = (
            diags(ql1) @ self.DL1
            + diags(qr1) @ self.DR1
            + diags(ql2) @ self.DL2
            + diags(qr2) @ self.DR2
        )
        return tmp1 - self.dt * (tmp2 - tmp3)

    def solve_HJB(self, M, Q):
        QL1, QR1, QL2, QR2 = Q  # unpack
        mT = M[-1, :]
        un = self.get_UT(mT)
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            ql1 = QL1[ti, :]
            qr1 = QR1[ti, :]
            ql2 = QL2[ti, :]
            qr2 = QR2[ti, :]
            q = [ql1, qr1, ql2, qr2]
            A = self.linearOP_HJB(q)
            rhs = self.hjb_rhs(un, q, mn)
            self.U[ti, :] = spsolve(A, rhs)
            un = self.U[ti, :]
        return

    def solve_HJB_fixp(self, M):
        """
        solve linearize HJB with hamilton:
        0.5*|Du|^2/F1(m) - F2(m)
        where Du is frezz with U_old

        this method should only update self.U
        """
        mT = M[-1, :]
        un = self.get_UT(mT)
        for ti in range(self.Nt - 1, -1, -1):
            u_old = self.U_old[ti, :]
            dul1_old = np.maximum(self.DL1 @ u_old, 0.0)
            dur1_old = np.minimum(self.DR1 @ u_old, 0.0)
            dul2_old = np.maximum(self.DL2 @ u_old, 0.0)
            dur2_old = np.minimum(self.DR2 @ u_old, 0.0)
            du2_old = dul1_old**2 + dur1_old**2 + dul2_old**2 + dur2_old**2
            mn = M[ti, :]
            lhsM = self.A_fixp
            rhs = self.hjb_rhs_fixp(un, du2_old, mn)
            self.U[ti, :] = spsolve(lhsM, rhs)
            un = self.U[ti, :]
        self.U_old = np.copy(self.U)
        return

    def update_Q(self, U, M):
        """
        this method should only update self.QL and self.QR
        """
        for ti in range(self.Nt):
            mn = M[ti, :]
            un = U[ti, :]
            dul1 = self.DL1 @ un
            dur1 = self.DR1 @ un
            dul2 = self.DL2 @ un
            dur2 = self.DR2 @ un
            self.QL1[ti, :] = np.maximum(self.optimal_control(mn, dul1), 0.0)
            self.QR1[ti, :] = np.minimum(self.optimal_control(mn, dur1), 0.0)
            self.QL2[ti, :] = np.maximum(self.optimal_control(mn, dul2), 0.0)
            self.QR2[ti, :] = np.minimum(self.optimal_control(mn, dur2), 0.0)
        self.QL1_old = np.copy(self.QL1)
        self.QR1_old = np.copy(self.QR1)
        self.QL2_old = np.copy(self.QL2)
        self.QR2_old = np.copy(self.QR2)
        self.Q_old = [self.QL1_old, self.QR1_old, self.QL2_old, self.QR2_old]
        return

    def default_fp_pn(n):
        if n == 0:
            return (0, 1)
        else:
            return (1 - 1 / (n + 1), 1 / (n + 1))

    def solve(self, maxit=10, fp=False, pn=default_fp_pn):
        # fp: bool, use fictious play or not
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(1, maxit + 1):
            # solve FP with Q
            Q = [self.QL1, self.QR1, self.QL2, self.QR2]
            self.solve_FP(Q)
            # update M_bar if use fictious play
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            # update U with M_bar and Q
            self.solve_HJB(self.M_bar, Q)
            # update Q with U and M_bar
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)
            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_spi1_pn(n):
        return (n / (n + 2), 1 / (n + 2))

    def solve_with_spi1(self, maxit=10, pn=default_spi1_pn):
        self.diff_M = []
        # init
        QL1_bar = np.copy(self.QL1)
        QR1_bar = np.copy(self.QR1)
        QL2_bar = np.copy(self.QL2)
        QR2_bar = np.copy(self.QR2)
        for i in range(0, maxit):
            # solve FP with Q_bar
            Q_bar = [QL1_bar, QR1_bar, QL2_bar, QR2_bar]
            self.solve_FP(Q_bar)
            # update U with M and Q_bar
            self.solve_HJB(self.M, Q_bar)
            # update Q with U and M
            self.update_Q(self.U, self.M)
            # update Q_bar
            p1, p2 = pn(i)
            QL1_bar = p1 * QL1_bar + p2 * self.QL1
            QR1_bar = p1 * QR1_bar + p2 * self.QR1
            QL2_bar = p1 * QL2_bar + p2 * self.QL2
            QR2_bar = p1 * QR2_bar + p2 * self.QR2
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def default_spi2_pn(n):
        if n == 0:
            return (0, 1)
        else:
            return (1 - 1 / (n + 1), 1 / (n + 1))

    def solve_with_spi2(self, maxit=10, pn=default_spi2_pn):
        self.diff_M = []
        # init
        QL1_hat = np.copy(self.QL1)
        QR1_hat = np.copy(self.QR1)
        QL2_hat = np.copy(self.QL2)
        QR2_hat = np.copy(self.QR2)
        self.M_bar = np.copy(self.M)
        # init W_bar, but never use this init value
        # update W_bar in first iteration with M*q
        # and average W in later iteration
        WL1_bar = np.copy(self.QL1)
        WR1_bar = np.copy(self.QR1)
        WL2_bar = np.copy(self.QL2)
        WR2_bar = np.copy(self.QR2)
        for i in range(0, maxit):
            # solve FP with Q
            Q = [self.QL1, self.QR1, self.QL2, self.QR2]
            self.solve_FP(Q)
            # update M_bar
            p1, p2 = pn(i)
            self.M_bar = p1 * self.M_bar + p2 * self.M
            # update Q_hat(firt compute W_bar)
            if p1 == 0:
                WL1_bar = self.M * self.QL1
                WR1_bar = self.M * self.QR1
                WL2_bar = self.M * self.QL2
                WR2_bar = self.M * self.QR2
                QL1_hat = np.copy(self.QL1)  # avoid error here
                QR1_hat = np.copy(self.QR1)
                QL2_hat = np.copy(self.QL2)
                QR2_hat = np.copy(self.QR2)
            else:
                WL1_bar = p1 * WL1_bar + p2 * self.M * self.QL1
                WR1_bar = p1 * WR1_bar + p2 * self.M * self.QR1
                WL2_bar = p1 * WL2_bar + p2 * self.M * self.QL2
                WR2_bar = p1 * WR2_bar + p2 * self.M * self.QR2
                QL1_hat = WL1_bar / self.M_bar  # be careful when M_bar is too small
                QR1_hat = WR1_bar / self.M_bar
                QL2_hat = WL2_bar / self.M_bar
                QR2_hat = WR2_bar / self.M_bar
            # update U with M and Q_hat
            Q_hat = [QL1_hat, QR1_hat, QL2_hat, QR2_hat]
            self.solve_HJB(self.M_bar, Q_hat)
            # update Q with U and M(don't consider M here)
            self.update_Q(self.U, self.M)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.M_old = np.copy(self.M)
            self.diff_M.append(diff_M)
            # use which M to compute residual?
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def solve_with_fixpoint(self, maxit=10, fp=False, pn=default_fp_pn):
        print("solving with fixed point method")
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(0, maxit):
            Q = [self.QL1, self.QR1, self.QL2, self.QR2]
            self.solve_FP(Q)
            if fp:
                p1, p2 = pn(i)
                self.M_bar = p1 * self.M_bar + p2 * self.M
            else:
                self.M_bar = self.M
            self.solve_HJB_fixp(self.M_bar)
            self.update_Q(self.U, self.M_bar)
            diff_M = np.max(np.abs(self.M - self.M_old))
            print(f"||M^(n+1)-M^(n)|| = {diff_M}")
            self.diff_M.append(diff_M)
            self.M_old = np.copy(self.M)

            diff_M_Mbar = np.max(np.abs(self.M - self.M_bar))
            self.diff_M_Mbar.append(diff_M_Mbar)
            self.compute_residual(self.M, self.U)
            self.logging_solution(self.M, self.U)
        return

    def compute_residual(self, M, U):
        res_fp = self.residual_FP(M, U)
        res_hjb = self.residual_HJB(M, U)
        self.residual_FP_history.append(res_fp)
        self.residual_HJB_history.append(res_hjb)
        return res_fp, res_hjb

    def residual_FP(self, M, U):
        residual_ = np.zeros_like(M)  # residual in every point
        mn = self.M0
        for ti in range(self.Nt):
            m = M[ti, :]
            un = U[ti, :]
            dul1 = self.DL1 @ un
            dur1 = self.DR1 @ un
            dul2 = self.DL2 @ un
            dur2 = self.DR2 @ un
            # q here is only a temp variable to compute residual
            ql1 = np.maximum(self.optimal_control(m, dul1), 0.0)
            qr1 = np.minimum(self.optimal_control(m, dur1), 0.0)
            ql2 = np.maximum(self.optimal_control(m, dul2), 0.0)
            qr2 = np.minimum(self.optimal_control(m, dur2), 0.0)
            q = [ql1, qr1, ql2, qr2]
            lhsM = self.linearOP_FP(q) / self.dt
            rhs = mn / self.dt
            residual_[ti, :] = lhsM @ m - rhs
            mn = M[ti, :]
        residual = np.sqrt(self.dx**2 * self.dt) * norm(residual_)
        return residual

    def residual_HJB(self, M, U):
        residual_ = np.zeros_like(U)  # residual in every point
        mT = M[-1, :]
        un = self.get_UT(mT)
        for ti in range(self.Nt - 1, -1, -1):
            mn = M[ti, :]
            u = U[ti, :]
            dul1 = self.DL1 @ u
            dur1 = self.DR1 @ u
            dul2 = self.DL2 @ u
            dur2 = self.DR2 @ u
            # q here is only a temp variable to compute residual
            ql1 = np.maximum(self.optimal_control(mn, dul1), 0.0)
            qr1 = np.minimum(self.optimal_control(mn, dur1), 0.0)
            ql2 = np.maximum(self.optimal_control(mn, dul2), 0.0)
            qr2 = np.minimum(self.optimal_control(mn, dur2), 0.0)
            q = [ql1, qr1, ql2, qr2]
            lhsM = self.linearOP_HJB(q) / self.dt
            rhs = self.hjb_rhs(un, q, mn) / self.dt
            residual_[ti, :] = lhsM @ u - rhs
            un = U[ti, :]
        residual = np.sqrt(self.dx**2 * self.dt) * norm(residual_)
        return residual

    def compute_cost(self):
        cost = 0.0
        mT = self.M[-1, :]
        uT = self.get_UT(mT)
        for ti in range(self.Nt):
            m = self.M[ti, :]
            u = self.U[ti, :]
            dul1 = self.DL1 @ u
            dur1 = self.DR1 @ u
            dul2 = self.DL2 @ u
            dur2 = self.DR2 @ u
            # q here is only a temp variable to compute residual
            ql1 = np.maximum(self.optimal_control(m, dul1), 0.0)
            qr1 = np.minimum(self.optimal_control(m, dur1), 0.0)
            ql2 = np.maximum(self.optimal_control(m, dul2), 0.0)
            qr2 = np.minimum(self.optimal_control(m, dur2), 0.0)
            q2 = ql1**2 + qr1**2 + ql2**2 + qr2**2
            cost += np.sum(
                self.dt
                * self.dx**2
                * m
                * (0.5 * self.F1_func(m) * q2 + self.F2_func(m))
            )
        cost += np.sum(self.dx**2 * uT * self.M[-1, :])
        return cost


def plot_residual(result, iterations: int):
    plt.plot(range(iterations), result.residual_FP_history, label="residual fp")
    plt.plot(range(iterations), result.residual_HJB_history, label="residual hjb")
    plt.yscale("log")
    plt.legend()
    plt.grid()
    plt.show()


def plot_sol_diff(bcmk, result):
    iterations = len(result.sol_M_history)
    diff_M = []
    diff_U = []
    for i in range(iterations):
        diff_M.append(np.max(np.abs(result.sol_M_history[i] - bcmk.M)))
        diff_U.append(np.max(np.abs(result.sol_U_history[i] - bcmk.U)))
    plt.plot(range(iterations), diff_M, label="|M^(n) - M^*|")
    plt.plot(range(iterations), diff_U, label="|U^(n) - U^*|")
    plt.yscale("log")
    plt.legend()
    plt.grid()
    plt.show()
