import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve, LinearOperator, gmres
from scipy.linalg import norm
from scipy.sparse import diags
import matplotlib.pyplot as plt
import types


class MfgErgodic(object):
    def __init__(
        self, Q_guess=None, nv=0.05, x1=0, x2=1, Nx=200, bc="periodic"
    ):
        if bc == "periodic":
            self.xs = np.linspace(x1, x2, Nx + 1)[:-1]  # grid on space
        elif bc == "dirichlet":
            self.xs = np.linspace(x1, x2, Nx + 1)[1:-1]  # grid on space
        elif bc == "neumann":
            self.xs = np.linspace(x1, x2, Nx + 1)  # grid on space
        self.Nx = self.xs.shape[0]
        self.dx = self.xs[1] - self.xs[0]
        self.nv = nv  # diffusion paramter   

        # array to store solution
        self.U = np.zeros(self.Nx)
        self.M = np.ones(self.Nx)
        self.lbda = 0.0
        self.M_old = np.copy(self.M)
        self.U_old = np.copy(self.U)

        # initial guess about Q
        if isinstance(Q_guess, types.FunctionType):
            q0 = Q_guess(self.xs)
            self.QL = np.maximum(q0, 0)
            self.QR = np.minimum(q0, 0)
        elif isinstance(Q_guess, np.ndarray):
            self.QL = np.copy(Q_guess[0])
            self.QR = np.copy(Q_guess[1])
        else:
            self.QL = np.zeros(self.Nx)
            self.QR = np.zeros(self.Nx)
        self.QL_old = np.copy(self.QL)
        self.QR_old = np.copy(self.QR)

        # some lists to log residual or something else
        self.residual_FP_history = []  # list to store history of residual
        self.residual_HJB_history = []  # list to store history of residual
        self.sol_M_history = []  # list to store history of L-inf disatance
        self.sol_U_history = []  # list to store history of L-2 disatance
        self.Laplace = self.build_Laplace(bc)
        self.DL, self.DR = self.build_D(bc)
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
            dim_one_laplace[0, 1] += 1
            dim_one_laplace[-1, -2] += 1
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
            DL[0, 1] += -1 / self.dx
            DL[-1, -2] += -1 / self.dx
            return DL, DR
        else:
            raise NotImplementedError("unsupported boundary condition")



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

    def logging_solution(self, M, U):
        self.sol_M_history.append(np.copy(M))
        self.sol_U_history.append(np.copy(U))
        return

    def linearOP_FP(self, q):
        ql, qr = q  # unpack
        tmp1 = sparse.eye(self.Nx)
        tmp2 = self.Laplace
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


    def solve(self, maxit=10):
        # fp: bool, use fictious play or not
        self.diff_M = []
        self.diff_M_Mbar = []
        for i in range(0, maxit):
            # solve FP with Q
            Q = [self.QL, self.QR]
            self.solve_FP(Q)

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

    def compute_residual(self, M, U, lbda):
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


        