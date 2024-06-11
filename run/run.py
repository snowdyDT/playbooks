from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play_context import PlayContext
from ansible.vars.manager import VariableManager

from run import config


def main():
    data_loader = DataLoader()
    inventory = InventoryManager(loader=data_loader, sources=[f"inventory/hosts.yml"])

    variable_manager = VariableManager(loader=data_loader, inventory=inventory)
    variable_manager.set_host_variable(inventory.get_host(config.hosts), "ansible_connection", "local")
    variable_manager.set_host_variable(inventory.get_host(config.hosts), "PYTHON_VENV_PATH", config.python_venv_path)
    variable_manager.set_host_variable(inventory.get_host(config.hosts), "PYTHON_LIBRARY", config.python_library)

    play_context = PlayContext()
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=data_loader,
        passwords={},
    )

    playbook_executor = PlaybookExecutor(
        playbooks=[config.playbook_path],
        inventory=inventory,
        variable_manager=variable_manager,
        loader=data_loader,
        passwords={},
    )

    result = playbook_executor.run()
    print(f'Playbook выполнен с кодом: {result}')


if __name__ == '__main__':
    main()
