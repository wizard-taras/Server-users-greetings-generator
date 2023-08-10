def reports_for_admin(no_of_active_users, traffic_stats, server_free_space_avail,
                      SSD_read_write_fails):
    reports_dict = {'Number of active users by now': no_of_active_users,
                    'Total traffic consumed by the users previuos day, MB': traffic_stats,
                    'Available free space on the server SSD disks, GiB': server_free_space_avail,
                    'Total SSD read/write fails': SSD_read_write_fails}
    return [print(key + ':', value) for key, value in reports_dict.items()]

users = ['taras', 'sidzo', 'phoebe', 'admin', 'serviceman', 'support_eng']
print(type(reports_for_admin(1225, 5578801, 557, 17)))