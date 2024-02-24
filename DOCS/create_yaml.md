### Создание yaml файлов

В рамках проекта VAIR доступны методы и их параметры для выполнения POST запросов, которые могут быть получены по ссылке узла http://{ip}/apidoc/swagger

- Метод для POST запроса api/v2/volumes/create/ будет называться volumes_create
- Параметры которые нужно передавать после объявления метода можно найти нажав в swagger кнопку "Try it out"


<details>
  <summary>Шаблонизатор в YAML</summary>

* Для создания нескольких элементов одного типа можно использовать символы "|" и "<". Это позволяет генерировать множественные записи.

    ### Пример:
    ```yaml
    volumes_create|10:
        format: "qcow2"
        name: "TEST<"
        pool_id: "POOL"
        size: "1"
        type: "thin"
        unit: "M"
    ```

    В данном примере указано в названии метода "volumes_create|10" и name: "TEST<", что означает создание 10 виртуальных дисков с именами TEST0, TEST1, TEST2 и т.д.

* Для поля pool_id можно указывать как UUID пула, так и его имя. Приложение автоматически конвертирует имя пула в его UUID формат.

    ### Пример:
    ``` yaml
    volumes_create:
        format: "qcow2"
        name: "TEST"
        pool_id: "6f0bf87a-4e93-44ad-9d98-f129c89ff780" # вместо UUID можно указать имя пула POOL
        size: "1"
        type: "thin"
        unit: "M"
    ```

* Для поля id виртуальных дисков на ARDFS пуле можно вместо UUID указать имя диска, добавив "volume_name>ИМЯ ДИСКА". Приложение автоматически подставит UUID диска.

    ### Пример:
    ```yaml
    volumes_delete:
        full_delete: "false"
        id: "volume_name>TEST" # вместо UUID диска
    ```
</details>

<details>
  <summary>Список методов POST</summary>

<details>
    <summary>acfs_create: Создание acfs пула.</summary>

```json
    {
        "description": "string", # описание пула
        "name": "string",        # имя пула
        "node": "string",        # выбор узла на котором будет запущен задача
        "wwn_disk": "string"     # wwn блочного устройства пригнаного по iscsi например 366c4a7404e47494e453032342c49470d
    }
```
</details>

* acfs_delete: Удаление acfs пула.
* acfs_disks_convert: Конвертация из vmdk в формат для VAIR.
* acfs_disks_copy: Копирование виртуального диска.
* acfs_disks_create: Создание виртуального диска на acfs пуле.
* acfs_disks_delete: Удаление виртуального диска на acfs пуле.
* acfs_disks_edit: Редактирование параметров виртуального диска на acfs пуле.
* acfs_disks_rescan: Пересканирование виртуальных дисков на acfs пуле.
* acfs_disks_resize: Изменение размера виртуального диска на acfs пуле.
* acfs_images_copy: Копирование образов.
* acfs_images_delete: Удаление образов.
* acfs_images_upload: Загрузка образов.
* acfs_images_uploadFile: Загрузка образа из файла.
* acfs_limit: Установка ограничений для acfs.
* acfs_mount: Монтирование acfs.
* acfs_umount: Размонтирование acfs.
* administration_role: Создание роли администратора.
* administration_rule: Создание правила администрирования.
* administration_user_group: Создание группы пользователей.
* administration_user: Создание пользователя.
* auth_login: Аутентификация пользователя.
* auth_logout: Выход пользователя из системы.
* auth_refresh_token: Обновление токена аутентификации.
* chrony_add_server: Добавление сервера для синхронизации времени с помощью Chrony.
* chrony_sync_time: Синхронизация времени с сервером Chrony.
* cluster_fs_bmc_check: Проверка состояния BMC кластера.
* cluster_fs_bmc_edit: Редактирование BMC кластера.
* cluster_fs_bmc_identity: Получение идентификатора BMC кластера.
* cluster_fs_bmc_power_off: Выключение питания BMC кластера.
* cluster_fs_bmc_power_on: Включение питания BMC кластера.
* cluster_fs_bmc_reset: Сброс BMC кластера.
* cluster_fs_power_off: Выключение питания кластера.
* cluster_fs_restart: Перезапуск кластера.
* fibre_channel_rescan: Пересканирование каналов Fibre Channel.
* iscsi_create: Создание iSCSI.
* iscsi_delete: Удаление iSCSI.
* iscsi_info_iqn_rescan: Пересканирование информации об iSCSI.
* iscsi_login: Логин в iSCSI.
* iscsi_logout: Логаут из iSCSI.
* iscsi_node_edit: Редактирование узла iSCSI.
* iscsi_rescan: Пересканирование iSCSI.
* luns_delete_label: Удаление метки LUN.
* luns_rescan: Пересканирование LUN.
* meta_disks_replace: Замена метадиска.
* meta_disks_rescan: Пересканирование метадисков.
* nfs_convert_mount: Конвертация монтирования NFS.
* nfs_convert_umount: Конвертация размонтирования NFS.
* nfs_add: Добавление NFS.
* nfs_delete: Удаление NFS.
* nfs_disks_convert: Конвертация дисков NFS.
* nfs_disks_copy: Копирование дисков NFS.
* nfs_disks_create: Создание дисков NFS.
* nfs_disks_delete: Удаление дисков NFS.
* nfs_disks_edit: Редактирование параметров дисков NFS.
* nfs_disks_rescan: Пересканирование дисков NFS.
* nfs_disks_resize: Изменение размера дисков NFS.
* nfs_images_copy: Копирование образов NFS.
* nfs_images_delete: Удаление образов NFS.
* nfs_images_upload: Загрузка образов NFS.
* nfs_images_uploadFile: Загрузка образа NFS из файла.
* nfs_limit: Установка ограничений для NFS.
* nfs_mount: Монтирование NFS.
* nfs_unmount: Размонтирование NFS.
* ntp_create: Создание сервера времени (NTP).
* ntp_sync_now: Синхронизация времени с сервером NTP.
* physical_disks_delete_label: Удаление метки с физического диска.
* physical_disks_delete_mountpoint: Удаление точки монтирования с физического диска.
* physical_disks_format: Форматирование физического диска.
* physical_disks_mount_driver: Монтирование драйвера на физический диск.
* physical_disks_rescan: Пересканирование физических дисков.
* physical_disks_unmount_driver: Размонтирование драйвера с физического диска.
* pools_create: Создание пула.
* pools_delete: Удаление пула.
* pools_limit: Установка ограничений для пула.
* pools_start: Запуск пула.
* pools_stop: Остановка пула.
* settings_change_adl_setting: Изменение настроек ADL.
* settings_change_app_protocol: Изменение протокола приложения.
* settings_change_iec_units: Изменение единиц измерения IEC.
* settings_change_mem_setting: Изменение настроек памяти.
* settings_upload_private_key: Загрузка приватного ключа.
* settings_upload_public_key: Загрузка публичного ключа.
* snmp_edit: Редактирование настроек SNMP.
* statistics_clear: Очистка статистики.
* statistics_download: Загрузка статистики.
* statistics_rotation: Вращение статистики.
* virtual_images_copy: Копирование виртуальных образов.
* virtual_images_delete: Удаление виртуальных образов.
* virtual_images_upload: Загрузка виртуальных образов.
* virtual_images_uploadFile: Загрузка виртуального образа из файла.
* virtual_machines_external_snapshots_create: Создание внешних снимков виртуальных машин.
* virtual_machines_external_snapshots_delete: Удаление внешних снимков виртуальных машин.
* virtual_machines_external_snapshots_rollback: Откат внешних снимков виртуальных машин.
* virtual_machines_external_snapshots_save: Сохранение внешних снимков виртуальных машин.
* virtual_machines_snapshots_create: Создание снимков виртуальных машин.
* virtual_machines_snapshots_delete: Удаление снимков виртуальных машин.
* virtual_machines_snapshots_rollback: Откат снимков виртуальных машин.
* virtual_machines_templates_delete: Удаление шаблонов виртуальных машин.
* virtual_machines_templates_edit: Редактирование шаблонов виртуальных машин.
* virtual_machines_templates_make_vm: Создание виртуальной машины из шаблона.
* virtual_machines_templates_migrate: Миграция шаблонов виртуальных машин.
* virtual_machines_accord_disable: Отключение согласования виртуальных машин.
* virtual_machines_accord_enable: Включение согласования виртуальных машин.
* virtual_machines_change_vnc_password: Изменение пароля VNC виртуальной машины.
* virtual_machines_clone: Клонирование виртуальной машины.
* virtual_machines_create: Создание виртуальной машины.
* virtual_machines_delete_vnc_password: Удаление пароля VNC виртуальной машины.
* virtual_machines_delete: Удаление виртуальной машины.
* virtual_machines_down: Остановка виртуальной машины.
* virtual_machines_edit: Редактирование параметров виртуальной машины.
* virtual_machines_migration: Миграция виртуальной машины.
* virtual_machines_restart: Перезапуск виртуальной машины.
* virtual_machines_resume: Возобновление работы виртуальной машины.
* virtual_machines_suspend: Приостановка виртуальной машины.
* virtual_machines_template: Установка виртуальной машины как шаблона.
* virtual_machines_up: Запуск виртуальной машины.
* virtual_networks_portgroup_create: Создание портгруппы виртуальных сетей.
* virtual_networks_portgroup_delete: Удаление портгруппы виртуальных сетей.
* virtual_networks_portgroup_edit: Редактирование параметров портгруппы виртуальных сетей.
* volumes_copy: Копирование томов.
* volumes_create: Создание томов.
* volumes_delete: Удаление томов.
* volumes_edit: Редактирование параметров томов.
* volumes_nfs_convert: Конвертация томов в формат VAIR.
* volumes_rescan: Пересканирование томов.
* volumes_resize: Изменение размера томов.
</details>

<details>
<summary>Список методов GET</summary>

* acfs: Получение информации о acfs.
* acfs_disks: Получение информации о дисках acfs.
* acfs_disks_free: Получение информации о свободных дисках acfs.
* acfs_images: Получение информации об образах acfs.
* administration_available_rules: Получение доступных правил администрирования.
* administration_role_role_id: Получение информации о роли администратора по идентификатору роли.
* administration_roles: Получение списка ролей администраторов.
* administration_rule_obj_type_obj_id: Получение правила администрирования по типу объекта и идентификатору объекта.
* administration_rule_rule_id: Получение правила администрирования по идентификатору правила.
* administration_rules: Получение списка правил администрирования.
* administration_user_group_group_id: Получение информации о группе пользователей по идентификатору группы.
* administration_user_groups: Получение списка групп пользователей.
* administration_user: Получение информации о пользователе.
* administration_user_user_id: Получение информации о пользователе по его идентификатору.
* administration_users: Получение списка пользователей.
* chrony: Получение информации о настройках Chrony.
* cluster_fs: Получение информации о файловых системах кластера.
* cluster_fs_sputnic: Получение информации о Sputnic.
* cpu: Получение информации о CPU.
* dashboard: Получение информации о дашборде.
* ethernet: Получение информации об Ethernet.
* fibre_channel: Получение информации о Fibre Channel.
* front_end_adapters: Получение информации о передних адаптерах.
* iscsi: Получение информации об iSCSI.
* iscsi_info_interface: Получение информации о интерфейсе iSCSI.
* iscsi_info_iqn: Получение информации об iSCSI IQN.
* jobs: Получение информации о заданиях.
* luns: Получение информации о LUN.
* luns_free: Получение информации о свободных LUN.
* memory_mode: Получение информации о режиме памяти.
* meta_disks: Получение информации о метадисках.
* network_interfaces: Получение информации о сетевых интерфейсах.
* nfs_convert_find_disks: Поиск дисков для конвертации в NFS.
* nfs_convert_state: Получение состояния конвертации в NFS.
* nfs: Получение информации о NFS.
* nfs_disks: Получение информации о дисках NFS.
* nfs_disks_free: Получение информации о свободных дисках NFS.
* nfs_images: Получение информации об образах NFS.
* nodes_time_offsets: Получение смещения времени узлов.
* nodes: Получение информации о узлах.
* ntp: Получение информации о NTP.
* os: Получение информации о операционной системе.
* physical_disks: Получение информации о физических дисках.
* physical_disks_free_mounted: Получение информации о свободных и примонтированных физических дисках.
* physical_disks_free: Получение информации о свободных физических дисках.
* pools: Получение информации о пулах.
* sensors: Получение информации о датчиках.
* services_logs_criticals: Получение критических записей логов служб.
* services_logs_tasks: Получение записей логов задач.
* services_logs_warnings: Получение предупреждений из логов служб.
* settings_adl: Получение настроек ADL.
* settings_get_app_protocol: Получение протокола приложения.
* settings_get_user_settings: Получение настроек пользователя.
* settings_memory_ram: Получение информации о памяти RAM.
* snmp: Получение информации о настройках SNMP.
* statistics_alerts: Получение статистики по предупреждениям.
* statistics_alerts_active: Получение активных предупреждений.
* task_task_id: Получение информации о задании по его идентификатору.
* tasks: Получение списка заданий.
* tasks_state: Получение состояния заданий.
* tasks_task_limit: Получение лимита заданий.
* virtual_images: Получение информации о виртуальных образах.
* virtual_machines_external_snapshots: Получение внешних снимков виртуальных машин.
* virtual_machines_external_snapshots_vm_id: Получение внешних снимков виртуальной машины по ее идентификатору.
* virtual_machines_snapshots: Получение снимков виртуальных машин.
* virtual_machines_templates: Получение информации о шаблонах виртуальных машин.
* virtual_machines: Получение информации о виртуальных машинах.
* virtual_machines_cpu_features_vm_id: Получение характеристик CPU виртуальной машины по ее идентификатору.
* virtual_machines_cpu_cpu_features: Получение характеристик CPU.
* virtual_machines_cpu_features: Получение характеристик CPU виртуальной машины.
* virtual_machines_cpu_models: Получение моделей CPU виртуальной машины.
* virtual_machines_network_interfaces_vm_id: Получение сетевых интерфейсов виртуальной машины по ее идентификатору.
* virtual_machines_vm_disks_vm_id: Получение дисков виртуальной машины по ее идентификатору.
* virtual_machines_vm_info_vm_id: Получение информации о виртуальной машине по ее идентификатору.
* virtual_machines_vm_id: Получение информации о виртуальной машине по ее идентификатору.
* virtual_networks: Получение информации о виртуальных сетях.
* vm_performance_mode_action_name: Получение режима производительности по имени действия.
* volumes: Получение информации о томах.
* volumes_free: Получение информации о свободных томах.
</details>
