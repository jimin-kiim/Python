
from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file
from ro import get_ro_jobs
from wwr import get_wwr_jobs
# indeed_jobs=get_indeed_jobs()
so_jobs = get_so_jobs()
wwr_jobs=get_wwr_jobs("python")
ro_jobs=get_ro_jobs("python")
# jobs=indeed_jobs+so_jobs
# jobs=wwr_jobs
jobs=ro_jobs+wwr_jobs+ro_jobs
print(jobs)
# save_to_file(jobs)
# CSV(Comma Seperated Values)