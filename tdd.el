(defun version-probe-tests ()
  (let ((rootdir "/Users/sixtynorth/projects/version_probe")
        ;;(dir (file-name-directory load-file-name))
        (filename (buffer-file-name (current-buffer)))
        (output-buffer "*version-probe-buffer*"))
    (when (string-prefix-p rootdir filename)
      (display-buffer output-buffer)
      (shell-command (format "cd %s && python3 -m unittest discover version_probe/test" rootdir) output-buffer)
      (with-current-buffer output-buffer
        (compilation-mode 1)))))

(add-hook 'after-save-hook 'version-probe-tests)
