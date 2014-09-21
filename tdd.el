;; -*- lexical-binding: t -*-

(require 'deferred)

(defun version-probe-tests ()
  (lexical-let ((rootdir "/Users/sixtynorth/projects/version_probe")
        ;;(dir (file-name-directory load-file-name))
        (filename (buffer-file-name (current-buffer)))
        (output-buffer "*version-probe-buffer*"))
    (when (string-prefix-p rootdir filename)
      (get-buffer-create output-buffer)
      
      (with-current-buffer output-buffer
        (read-only-mode 0)
        (erase-buffer))
      
      (deferred:$

        (deferred:$
          (deferred:process-shell
            (format "cd %s && python3 -m unittest discover version_probe/test" rootdir)))

        ;; error
        (deferred:error it
          (lambda (err) (error-message-string err)))

        ;; finally
        (deferred:nextc it
          (lambda (x) x))
        
        (deferred:nextc it
          (lambda (output)
            (with-current-buffer output-buffer
              (insert output)
              (compilation-mode 1))
            (display-buffer output-buffer)))))))

(add-hook 'after-save-hook 'version-probe-tests)
