# (C) Datadog, Inc. 2024-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

from datadog_checks.dev import get_here

HERE = get_here()
USE_FLY_LAB = os.environ.get("USE_FLY_LAB")
COMPOSE_FILE = os.path.join(HERE, 'docker', 'docker-compose.yaml')
FLY_ACCESS_TOKEN = os.environ.get('FLY_ACCESS_TOKEN')
ORG_SLUG = os.environ.get('FLY_ORG_SLUG')

INSTANCE = {
    'org_slug': 'test',
    'openmetrics_endpoint': 'http://localhost:8080/metrics',
    'headers': {'Authorization': 'Bearer Test'},
}

LAB_INSTANCE = {
    'org_slug': ORG_SLUG,
    'headers': {'Authorization': f'Bearer {FLY_ACCESS_TOKEN}'},
}

MOCKED_METRICS = {
    "fly_io.instance.cpu",
    "fly_io.instance.disk.io_in_progress",
    "fly_io.instance.disk.reads_completed",
    "fly_io.instance.disk.reads_merged",
    "fly_io.instance.disk.sectors_read",
    "fly_io.instance.disk.sectors_written",
    "fly_io.instance.disk.time_io",
    "fly_io.instance.disk.time_io_weighted",
    "fly_io.instance.disk.time_reading",
    "fly_io.instance.disk.time_writing",
    "fly_io.instance.disk.writes_completed",
    "fly_io.instance.disk.writes_merged",
    "fly_io.instance.filefd.allocated",
    "fly_io.instance.filefd.max",
    "fly_io.instance.filesystem.block_size",
    "fly_io.instance.filesystem.blocks",
    "fly_io.instance.filesystem.blocks_avail",
    "fly_io.instance.filesystem.blocks_free",
    "fly_io.instance.load.avg",
    "fly_io.instance.memory.active",
    "fly_io.instance.memory.buffers",
    "fly_io.instance.memory.cached",
    "fly_io.instance.memory.dirty",
    "fly_io.instance.memory.inactive",
    "fly_io.instance.memory.mem_available",
    "fly_io.instance.memory.mem_free",
    "fly_io.instance.memory.mem_total",
    "fly_io.instance.memory.shmem",
    "fly_io.instance.memory.slab",
    "fly_io.instance.memory.swap_cached",
    "fly_io.instance.memory.swap_free",
    "fly_io.instance.memory.swap_total",
    "fly_io.instance.memory.vmalloc_chunk",
    "fly_io.instance.memory.vmalloc_total",
    "fly_io.instance.memory.vmalloc_used",
    "fly_io.instance.memory.writeback",
    "fly_io.instance.net.recv_bytes",
    "fly_io.instance.net.recv_compressed",
    "fly_io.instance.net.recv_drop",
    "fly_io.instance.net.recv_errs",
    "fly_io.instance.net.recv_fifo",
    "fly_io.instance.net.recv_frame",
    "fly_io.instance.net.recv_multicast",
    "fly_io.instance.net.recv_packets",
    "fly_io.instance.net.sent_bytes",
    "fly_io.instance.net.sent_carrier",
    "fly_io.instance.net.sent_colls",
    "fly_io.instance.net.sent_compressed",
    "fly_io.instance.net.sent_drop",
    "fly_io.instance.net.sent_errs",
    "fly_io.instance.net.sent_fifo",
    "fly_io.instance.net.sent_packets",
    "fly_io.instance.up",
    "fly_io.instance.memory.pressure_full",
    "fly_io.instance.memory.pressure_some",
}
