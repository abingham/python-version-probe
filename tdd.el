(defun version-probe-tests ()
  (let (;(dir (file-name-directory load-file-name))
        (buff "*version-probe-buffer*"))
    (display-buffer buff)
    (shell-command (format "cd /Users/sixtynorth/projects/version_probe && python3 -m unittest discover version_probe/test") buff)))

(add-hook 'after-save-hook 'version-probe-tests)
