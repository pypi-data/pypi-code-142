import os
import subprocess
from typing import Optional

from .. import contract, exceptions


class AptosContract(contract.BaseSmartContract):
    def compile(
        self,
        module_name: str,
        move_toml_dir: str,
        named_address: str,
        *,
        aptos_cli_dir: Optional[str] = None,
        output_dir: Optional[str] = None,
        save_metadata: bool = True,
    ):
        if aptos_cli_dir:
            aptos_cli_file_path = f"{aptos_cli_dir}/aptos"
        else:
            aptos_cli_file_path = "aptos"

        if not os.path.exists(aptos_cli_file_path):
            raise exceptions.CompilerError(
                f"Cannot find the APTOS cli: {aptos_cli_file_path}"
            )

        inline_cmd = f"{aptos_cli_file_path} move compile"

        if save_metadata:
            inline_cmd = f"{inline_cmd} --save-metadata"

        if "::" in module_name:
            module_name = module_name.split("::")[0]

        inline_cmd = f"{inline_cmd} --named-address {module_name}={named_address}"

        if move_toml_dir:
            inline_cmd = f"{inline_cmd} --package-dir {move_toml_dir}"

        if output_dir:
            inline_cmd = f"{inline_cmd} --output-dir {output_dir}"

        return super().compile()
